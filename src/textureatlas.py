import pygame

class TextureAtlas:
    def __init__(self, atlas_path: str):
        self.atlas_path = atlas_path
        self.image = pygame.image.load(atlas_path)

    def get_sprite(self, x: int, y: int) -> pygame.Surface:
        return self.image.subsurface((x * 100, y * 100, 100, 100))
