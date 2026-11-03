import math

import pygame


class Ball:
    def __init__(self, x, y, radius, vx=0.0, vy=0.0):
        self.x = float(x)
        self.y = float(y)
        self.radius = radius
        self.vx = float(vx)
        self.vy = float(vy)

    @property
    def speed(self):
        return math.hypot(self.vx, self.vy)

    @property
    def rect(self):
        r = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        r.center = (round(self.x), round(self.y))
        return r

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def bounce_walls(self, width):
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = abs(self.vx)
        elif self.x + self.radius > width:
            self.x = width - self.radius
            self.vx = -abs(self.vx)
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = abs(self.vy)

    def is_out(self, height):
        return self.y - self.radius > height
