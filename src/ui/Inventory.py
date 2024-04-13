import pygame

from src.ui.UIPanel import UIPanel

TILE_SIZE = 100

class Inventory(UIPanel):
    def __init__(self, rows: int, cols: int, inventory_tile: pygame.Surface):
        super().__init__((cols * TILE_SIZE, rows * TILE_SIZE))
        self.rows = rows
        self.cols = cols
        self.inventory_tile = inventory_tile

    def render_self(self, surface: pygame.Surface, position: tuple[int, int]):
        x, y = position

        slot_locations = []
        for row in range(self.rows):
            for col in range(self.cols):
                surface.blit(self.inventory_tile, (x + (col * TILE_SIZE), y + (row * TILE_SIZE)))

