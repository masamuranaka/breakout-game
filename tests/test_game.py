import pytest

from breakout.ball import Ball
from breakout.brick import Brick
from breakout.game import Game, GameState


@pytest.fixture
def game():
    return Game(width=800, height=600)


def test_initial_state_is_ready(game):
    assert game.state == GameState.READY
    assert game.score == 0
    assert game.lives == 3
    assert len(game.bricks) > 0


def test_ball_follows_paddle_while_ready(game):
    game.update(direction=1, dt=0.1)
    assert game.ball.x == pytest.approx(game.paddle.rect.centerx)
    assert game.ball.y < game.paddle.rect.top


def test_launch_starts_playing(game):
    game.launch()
    assert game.state == GameState.PLAYING
    assert game.ball.vy < 0


def test_ball_bounces_off_paddle(game):
    game.launch()
    game.bricks = []
    game.ball = Ball(x=game.paddle.rect.centerx, y=game.paddle.rect.top - 2,
                     radius=8, vx=0, vy=300)
    game.update(direction=0, dt=0.016)
    assert game.ball.vy < 0
    assert game.ball.y + game.ball.radius <= game.paddle.rect.top


def test_paddle_hit_position_changes_angle(game):
    game.launch()
    game.bricks = []
    right_edge = game.paddle.rect.right - 5
    game.ball = Ball(x=right_edge, y=game.paddle.rect.top - 2, radius=8, vx=0, vy=300)
    game.update(direction=0, dt=0.016)
    assert game.ball.vx > 0


def test_ball_destroys_brick_and_scores(game):
    game.launch()
    brick = Brick(x=100, y=100, width=60, height=20)
    game.bricks = [brick, Brick(x=600, y=50, width=60, height=20)]
    game.ball = Ball(x=130, y=125, radius=8, vx=0, vy=-300)
    game.update(direction=0, dt=0.016)
    assert not brick.alive
    assert brick not in game.bricks
    assert game.score == 10
    assert game.ball.vy > 0


def test_losing_ball_decrements_lives(game):
    game.launch()
    game.ball = Ball(x=400, y=game.height + 50, radius=8, vx=0, vy=300)
    game.update(direction=0, dt=0.016)
    assert game.lives == 2
    assert game.state == GameState.READY


def test_game_over_when_no_lives(game):
    game.launch()
    game.lives = 1
    game.ball = Ball(x=400, y=game.height + 50, radius=8, vx=0, vy=300)
    game.update(direction=0, dt=0.016)
    assert game.lives == 0
    assert game.state == GameState.GAME_OVER


def test_clear_when_all_bricks_destroyed(game):
    game.launch()
    brick = Brick(x=100, y=100, width=60, height=20)
    game.bricks = [brick]
    game.ball = Ball(x=130, y=125, radius=8, vx=0, vy=-300)
    game.update(direction=0, dt=0.016)
    assert game.state == GameState.CLEAR


def test_launch_is_ignored_when_game_over(game):
    game.state = GameState.GAME_OVER
    game.launch()
    assert game.state == GameState.GAME_OVER


def test_reset_restores_initial_state(game):
    game.launch()
    game.score = 500
    game.lives = 0
    game.state = GameState.GAME_OVER
    game.reset()
    assert game.state == GameState.READY
    assert game.score == 0
    assert game.lives == 3


def test_paused_game_does_not_move_ball(game):
    game.launch()
    game.toggle_pause()
    assert game.state == GameState.PAUSED
    x, y = game.ball.x, game.ball.y
    game.update(direction=0, dt=0.1)
    assert (game.ball.x, game.ball.y) == (x, y)
    game.toggle_pause()
    assert game.state == GameState.PLAYING
