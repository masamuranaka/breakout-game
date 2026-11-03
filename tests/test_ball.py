import pytest

from breakout.ball import Ball


def test_ball_moves_by_velocity():
    b = Ball(x=100, y=100, radius=8, vx=100, vy=-200)
    b.update(dt=0.5)
    assert b.x == pytest.approx(150)
    assert b.y == pytest.approx(0)


def test_ball_bounces_off_left_wall():
    b = Ball(x=5, y=100, radius=8, vx=-100, vy=0)
    b.bounce_walls(width=800)
    assert b.vx > 0
    assert b.x == pytest.approx(8)


def test_ball_bounces_off_right_wall():
    b = Ball(x=798, y=100, radius=8, vx=100, vy=0)
    b.bounce_walls(width=800)
    assert b.vx < 0
    assert b.x == pytest.approx(792)


def test_ball_bounces_off_ceiling():
    b = Ball(x=100, y=3, radius=8, vx=0, vy=-100)
    b.bounce_walls(width=800)
    assert b.vy > 0
    assert b.y == pytest.approx(8)


def test_ball_is_out_when_below_bottom():
    b = Ball(x=100, y=620, radius=8, vx=0, vy=100)
    assert b.is_out(height=600)


def test_ball_is_not_out_inside_screen():
    b = Ball(x=100, y=300, radius=8, vx=0, vy=100)
    assert not b.is_out(height=600)


def test_ball_rect_matches_position():
    b = Ball(x=100, y=100, radius=8, vx=0, vy=0)
    assert b.rect.center == (100, 100)
    assert b.rect.width == 16


def test_ball_speed_is_preserved_on_wall_bounce():
    b = Ball(x=5, y=3, radius=8, vx=-30, vy=-40)
    b.bounce_walls(width=800)
    assert b.speed == pytest.approx(50)
