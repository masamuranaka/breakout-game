from breakout.brick import Brick, create_brick_grid


def test_brick_is_alive_by_default():
    b = Brick(x=0, y=0, width=50, height=20)
    assert b.alive


def test_brick_hit_destroys_single_hp_brick():
    b = Brick(x=0, y=0, width=50, height=20)
    b.hit()
    assert not b.alive


def test_brick_with_multiple_hp_survives_one_hit():
    b = Brick(x=0, y=0, width=50, height=20, hp=2)
    b.hit()
    assert b.alive
    b.hit()
    assert not b.alive


def test_create_brick_grid_count():
    bricks = create_brick_grid(rows=5, cols=10, screen_width=800, top=60)
    assert len(bricks) == 50


def test_create_brick_grid_fits_in_screen():
    bricks = create_brick_grid(rows=5, cols=10, screen_width=800, top=60)
    assert all(0 <= b.rect.left and b.rect.right <= 800 for b in bricks)
    assert all(b.rect.top >= 60 for b in bricks)


def test_create_brick_grid_no_overlap():
    bricks = create_brick_grid(rows=3, cols=4, screen_width=800, top=60)
    for i, a in enumerate(bricks):
        for b in bricks[i + 1:]:
            assert not a.rect.colliderect(b.rect)
