from src.entity.Entity import Entity
from uuid import UUID
from src.entity.Character import Character
from src.textureatlas import TextureAtlas
import math

class FoodObj(Entity):
    def __init__(self, texture_atlas: TextureAtlas, textures: dict[str, tuple[int, int] | list[tuple[int, int]]], initial_texture: str, id: UUID | None = None):
        super().__init__(texture_atlas, textures, initial_texture, id)
        self.consumed=False

    def pickedUp(self, character: Entity):
        if not self.consumed:
            character.health = min(character.health+5,100)
            character.hunger = min(character.hunger+6,100)
            self.consumed = True

    def moveTowardEntity(self, target: Entity, deltatime: float):
        vecToEn = (target.position[0]-self.position[0], target.position[1]-self.position[1])
        length = math.sqrt(vecToEn[0]*vecToEn[0] + vecToEn[1]*vecToEn[1])
        vecToEn = (vecToEn[0]/length, vecToEn[1]/length)
        self.moveDir((vecToEn[0], vecToEn[1]), deltatime)
        if (length<5):
            self.pickedUp(target)
