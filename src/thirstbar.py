import pygame
class ThirstBar():
    def __init__(self, x, y, w, h, max_thirst):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.thirst = max_thirst
        self.max_thirst = max_thirst
        pass

    def render_self(self, surface: pygame.Surface):
        ratio = self.thirst / self.max_thirst
        pygame.draw.rect(surface, (56, 55, 50), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (40, 71, 156), (self.x, self.y, self.w * ratio, self.h))
