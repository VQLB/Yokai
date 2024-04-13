import pygame
class HungerBar():
     def __init__(self, x, y, w, h, max_hunger):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hunger = max_hunger
        self.max_hunger = max_hunger
        pass

     def render_self(self, surface: pygame.Surface):
        ratio = self.hunger / self.max_hunger
        pygame.draw.rect(surface, (56, 55, 50), (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, (191, 83, 6), (self.x, self.y, self.w * ratio, self.h))
        