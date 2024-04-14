import pygame

class StartScreen():
    def __init__(self):
        self.active = True


    def render_self(self, surface: pygame.Surface):
        surface.blit(pygame.image.load('asset/starting_screen.png'), (0,0))



