import pygame

class StartScreen():
    def __init__(self):
        self.active = True


    def render_self(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (34, 48, 38), (0, 0, 1920, 1080))



