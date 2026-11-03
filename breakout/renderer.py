import pygame

from breakout.game import GameState


class Renderer:
    BG_COLOR = (20, 24, 36)
    PADDLE_COLOR = (236, 240, 241)
    BALL_COLOR = (255, 255, 255)
    TEXT_COLOR = (236, 240, 241)

    MESSAGES = {
        GameState.READY: "SPACE でボール発射",
        GameState.PAUSED: "PAUSE  (P で再開)",
        GameState.GAME_OVER: "GAME OVER  (R でリトライ)",
        GameState.CLEAR: "CLEAR!  (R でもう一度)",
    }

    def __init__(self, surface):
        self.surface = surface
        self.font = self._load_font(28)
        self.small_font = self._load_font(22)

    @staticmethod
    def _load_font(size):
        # 日本語を表示できるフォントを優先して探す
        for name in ("hiraginosans", "hiraginokakugothicpro", "yugothic", "meiryo",
                     "notosanscjkjp", "notosansjp"):
            path = pygame.font.match_font(name)
            if path:
                return pygame.font.Font(path, size)
        return pygame.font.Font(None, size)

    def draw(self, game):
        s = self.surface
        s.fill(self.BG_COLOR)
        for brick in game.bricks:
            pygame.draw.rect(s, brick.color, brick.rect, border_radius=3)
        pygame.draw.rect(s, self.PADDLE_COLOR, game.paddle.rect, border_radius=6)
        pygame.draw.circle(s, self.BALL_COLOR, (round(game.ball.x), round(game.ball.y)),
                           game.ball.radius)

        hud = self.small_font.render(f"SCORE {game.score}    LIVES {game.lives}",
                                     True, self.TEXT_COLOR)
        s.blit(hud, (20, 20))

        message = self.MESSAGES.get(game.state)
        if message:
            text = self.font.render(message, True, self.TEXT_COLOR)
            s.blit(text, text.get_rect(center=(game.width // 2, game.height // 2 + 60)))
