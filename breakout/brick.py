import pygame

ROW_COLORS = [
    (231, 76, 60),
    (230, 126, 34),
    (241, 196, 15),
    (46, 204, 113),
    (52, 152, 219),
    (155, 89, 182),
]


class Brick:
    def __init__(self, x, y, width, height, hp=1, color=(200, 200, 200), points=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.hp = hp
        self.color = color
        self.points = points

    @property
    def alive(self):
        return self.hp > 0

    def hit(self):
        self.hp -= 1


def create_brick_grid(rows, cols, screen_width, top, margin=20, gap=4, height=20):
    width = (screen_width - margin * 2 - gap * (cols - 1)) // cols
    total = width * cols + gap * (cols - 1)
    left = (screen_width - total) // 2
    bricks = []
    for r in range(rows):
        color = ROW_COLORS[r % len(ROW_COLORS)]
        points = (rows - r) * 10
        for c in range(cols):
            x = left + c * (width + gap)
            y = top + r * (height + gap)
            bricks.append(Brick(x, y, width, height, color=color, points=points))
    return bricks
