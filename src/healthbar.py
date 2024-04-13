import pygame
class HealthBar():
    def __init__(self, x, y, w, h, max_health):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = max_health
        self.max_health = max_health
        pass

    def render_self(self, surface: pygame.Surface):
        ratio = self.health / self.max_health
        pygame.draw.rect(surface, (143, 13, 13), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (9, 77, 5), (self.x, self.y, self.w * ratio, self.h))
