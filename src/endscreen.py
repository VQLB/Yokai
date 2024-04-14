import pygame

class EndScreen():
    def __init__(self):
        self.active = False

    def render_self(self, surface: pygame.Surface):
        surface.blit(pygame.image.load('asset/ending_screen.png'), (0, 0))