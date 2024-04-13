import pygame


class UIPanel:
    def __init__(self, dimensions: tuple[int, int]):
        self.dimensions = dimensions

    def render_self(self, surface: pygame.Surface, position: tuple[int, int]):
        pass
