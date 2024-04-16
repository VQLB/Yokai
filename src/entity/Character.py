from src.entity.Entity import Entity
from uuid import UUID

from src.textureatlas import TextureAtlas


class Character(Entity):
    def __init__(self, texture_atlas: TextureAtlas, textures: dict[str, tuple[int, int] | list[tuple[int, int]]], initial_texture: str, id: UUID | None = None):
        super().__init__(texture_atlas, textures, initial_texture, id)
        self.hunger = 100

