import pygame
from cameraObj import Camera
from textureatlas import TextureAtlas
import pygame as pg
from uuid import UUID
import uuid
import math

class Entity:
    def __init__(self, texturePath: str,id: UUID | None = None):
        if not id:
            id = uuid.uuid4()
        self.id = id
        self.textureAtlas = TextureAtlas(texturePath)
        self.position = list((0,0))
        self.collidable = True
        self.health = 100
        self.displayName = "Entity"
        self.speed = 1

    def modifyHealth(self, offset):
        self.health += offset

    def moveDir(self, vecDir: tuple[float, float]):
        length = math.sqrt(vecDir[0]*vecDir[0] + vecDir[1]*vecDir[1])
        if length>0:
            normalizedVec = (vecDir[0]/length, vecDir[1]/length)
            self.position[0] += normalizedVec[0] * self.speed
            self.position[1] += normalizedVec[1] * self.speed

    def render_self(self, screen: pygame.Surface, camera: Camera):
        TextureSur = self.textureAtlas.get_sprite((0,0))
        screenPos = camera.convertWorldToScreen(self.position, screen)
        mapSize = TextureSur.get_size()
        screen.blit(pg.transform.scale(TextureSur, (mapSize[0] * camera.zoom, mapSize[1] * camera.zoom)),
                    screenPos)

