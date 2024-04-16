from src.entity.Entity import Entity
from uuid import UUID
import math

from src.textureatlas import TextureAtlas


class Enemy(Entity):
    def __init__(self, texture_atlas: TextureAtlas, textures: dict[str, tuple[int, int] | list[tuple[int, int]]], initial_texture: str, id: UUID | None = None):
        super().__init__(texture_atlas, textures, initial_texture, id)
        self.hurtFreezeTimer = 0

    def moveTowardEntity(self, target: Entity, deltatime: float):
        if self.hurtFreezeTimer <= 0:
            vecToEn = (target.position[0]-self.position[0], target.position[1]-self.position[1])

            if (vecToEn[0]>1):
                self.current_texture = "move_left"
            else:
                self.current_texture = "move_right"

            length = math.sqrt(vecToEn[0]*vecToEn[0] + vecToEn[1]*vecToEn[1])
            vecToEn = (vecToEn[0]/length, vecToEn[1]/length)
            self.moveDir((vecToEn[0], vecToEn[1]), deltatime)
        else:
            self.hurtFreezeTimer-=1
            self.current_texture = "hurt"
