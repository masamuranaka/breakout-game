import math
from enum import Enum, auto

from breakout.ball import Ball
from breakout.brick import create_brick_grid
from breakout.paddle import Paddle

BALL_SPEED = 400
MAX_BOUNCE_ANGLE = math.radians(60)


class GameState(Enum):
    READY = auto()
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    CLEAR = auto()


class Game:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.score = 0
        self.lives = 3
        self.paddle = Paddle(x=(self.width - 100) // 2, y=self.height - 40,
                             width=100, height=12, speed=500, screen_width=self.width)
        self.ball = Ball(0, 0, radius=8)
        self.bricks = create_brick_grid(rows=6, cols=10, screen_width=self.width, top=60)
        self._ready()

    def _ready(self):
        self.state = GameState.READY
        self._stick_ball_to_paddle()

    def _stick_ball_to_paddle(self):
        self.ball.x = self.paddle.rect.centerx
        self.ball.y = self.paddle.rect.top - self.ball.radius - 1
        self.ball.vx = 0.0
        self.ball.vy = 0.0

    def launch(self):
        if self.state != GameState.READY:
            return
        self.state = GameState.PLAYING
        angle = math.radians(20)
        self.ball.vx = BALL_SPEED * math.sin(angle)
        self.ball.vy = -BALL_SPEED * math.cos(angle)

    def toggle_pause(self):
        if self.state == GameState.PLAYING:
            self.state = GameState.PAUSED
        elif self.state == GameState.PAUSED:
            self.state = GameState.PLAYING

    def update(self, direction, dt):
        if self.state == GameState.READY:
            self.paddle.update(direction, dt)
            self._stick_ball_to_paddle()
            return
        if self.state != GameState.PLAYING:
            return

        self.paddle.update(direction, dt)
        self.ball.update(dt)
        self.ball.bounce_walls(self.width)
        self._collide_paddle()
        self._collide_bricks()

        if not self.bricks:
            self.state = GameState.CLEAR
        elif self.ball.is_out(self.height):
            self.lives -= 1
            if self.lives <= 0:
                self.state = GameState.GAME_OVER
            else:
                self._ready()

    def _collide_paddle(self):
        paddle = self.paddle.rect
        if self.ball.vy <= 0 or not self.ball.rect.colliderect(paddle):
            return
        offset = (self.ball.x - paddle.centerx) / (paddle.width / 2)
        offset = max(-1.0, min(1.0, offset))
        angle = offset * MAX_BOUNCE_ANGLE
        speed = self.ball.speed or BALL_SPEED
        self.ball.vx = speed * math.sin(angle)
        self.ball.vy = -speed * math.cos(angle)
        self.ball.y = paddle.top - self.ball.radius

    def _collide_bricks(self):
        ball_rect = self.ball.rect
        for brick in self.bricks:
            if not ball_rect.colliderect(brick.rect):
                continue
            brick.hit()
            # 重なりが小さい方の軸で反射させる
            overlap_x = min(ball_rect.right, brick.rect.right) - max(ball_rect.left, brick.rect.left)
            overlap_y = min(ball_rect.bottom, brick.rect.bottom) - max(ball_rect.top, brick.rect.top)
            if overlap_x < overlap_y:
                self.ball.vx = -self.ball.vx
            else:
                self.ball.vy = -self.ball.vy
            if not brick.alive:
                self.score += brick.points
            break
        self.bricks = [b for b in self.bricks if b.alive]
