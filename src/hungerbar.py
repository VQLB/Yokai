import pygame

class HealthBar():
     def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
        pass
     def render_self(self, surface: pygame.Surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, (204, 20, 20), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (12, 128, 6), (self.x, self.y, self.w * ratio, self.h))
        