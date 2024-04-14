import pygame

class EndScreen():
    def __init__(self):
        self.active = False


    def render_self(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (34, 48, 38), (0, 0, 800, 800))