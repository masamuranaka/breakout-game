from breakout.paddle import Paddle


def make_paddle():
    return Paddle(x=100, y=550, width=100, height=10, speed=300, screen_width=800)


def test_paddle_initial_position():
    p = make_paddle()
    assert p.rect.x == 100
    assert p.rect.y == 550
    assert p.rect.width == 100


def test_paddle_moves_left():
    p = make_paddle()
    p.update(direction=-1, dt=0.1)
    assert p.rect.x == 70


def test_paddle_moves_right():
    p = make_paddle()
    p.update(direction=1, dt=0.1)
    assert p.rect.x == 130


def test_paddle_does_not_move_without_input():
    p = make_paddle()
    p.update(direction=0, dt=0.1)
    assert p.rect.x == 100


def test_paddle_clamped_to_left_edge():
    p = make_paddle()
    p.update(direction=-1, dt=10)
    assert p.rect.left == 0


def test_paddle_clamped_to_right_edge():
    p = make_paddle()
    p.update(direction=1, dt=10)
    assert p.rect.right == 800
