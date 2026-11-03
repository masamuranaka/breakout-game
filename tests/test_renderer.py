import pygame
import pytest

from breakout.game import Game, GameState
from breakout.renderer import Renderer


@pytest.fixture(scope="module", autouse=True)
def pygame_init():
    pygame.init()
    yield
    pygame.quit()


@pytest.mark.parametrize("state", list(GameState))
def test_render_all_states_without_error(state):
    game = Game(800, 600)
    game.state = state
    surface = pygame.Surface((800, 600))
    Renderer(surface).draw(game)


def test_render_draws_paddle_color():
    game = Game(800, 600)
    surface = pygame.Surface((800, 600))
    renderer = Renderer(surface)
    renderer.draw(game)
    p = game.paddle.rect
    assert surface.get_at((p.centerx, p.centery))[:3] == renderer.PADDLE_COLOR
