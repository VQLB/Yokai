import pygame

class StatusBar:
    def __init__(
            self,
            position: tuple[int, int],
            dimensions: tuple[int, int],
            max_value: int,
            bar_color: tuple[float, float, float],
            background_color: tuple[float, float, float]
    ):
        self.position = position
        self.dimensions = dimensions
        self.value = max_value
        self.max_value = max_value
        self.bar_color = bar_color
        self.background_color = background_color
        pass

    def render_self(self, surface: pygame.Surface):
        ratio = self.value / self.max_value
        width, height = self.dimensions
        scaled_dimensions = (width * ratio, height)
        pygame.draw.rect(surface, self.background_color, (self.position, self.dimensions))
        pygame.draw.rect(surface, self.bar_color, (self.position, scaled_dimensions))
