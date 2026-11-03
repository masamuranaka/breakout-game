import pygame


class Paddle:
    def __init__(self, x, y, width, height, speed, screen_width):
        self.x = float(x)
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.screen_width = screen_width

    def update(self, direction, dt):
        self.x += direction * self.speed * dt
        self.x = max(0.0, min(self.x, self.screen_width - self.rect.width))
        self.rect.x = round(self.x)

    def center_at(self, x):
        self.x = max(0.0, min(x - self.rect.width / 2, self.screen_width - self.rect.width))
        self.rect.x = round(self.x)
