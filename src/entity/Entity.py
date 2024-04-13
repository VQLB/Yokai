import pygame
from cameraObj import Camera
from textureatlas import TextureAtlas
import pygame as pg
from uuid import UUID
import uuid
import math
from src.collider import collider

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
        self.speed = 50

    def modifyHealth(self, offset):
        self.health += offset

    def isCollidingWith(self, colliderObj: collider):
        xmin1, ymin1 = colliderObj.position
        width1, height1 = colliderObj.size

        xmin2, ymin2 = self.position
        width2, height2 = 100,100

        return ((xmin1 + width1 >= xmin2 and xmin2 + width2 >= xmin1) and (ymin1 + height1 >= ymin2 and ymin2 + height2 >= ymin1))

    def resolveCollision(self, colliderObj: collider):
        if self.isCollidingWith(colliderObj):
            xLeft = self.position[0] - (colliderObj.position[0] + colliderObj.size[0])
            xRight =
            print(xLeft)


    def moveDir(self, vecDir: tuple[float, float], deltaTime: float):
        length = math.sqrt(vecDir[0]*vecDir[0] + vecDir[1]*vecDir[1])
        if length>0:
            normalizedVec = (vecDir[0]/length, vecDir[1]/length)
            self.position[0] += normalizedVec[0] * self.speed * max(0.0001,deltaTime)
            self.position[1] += normalizedVec[1] * self.speed * max(0.0001,deltaTime)

    def render_self(self, screen: pygame.Surface, camera: Camera):
        TextureSur = self.textureAtlas.get_sprite((0,0))
        screenPos = camera.convertWorldToScreen(self.position, screen)
        mapSize = TextureSur.get_size()
        screen.blit(pg.transform.scale(TextureSur, (mapSize[0] * camera.zoom, mapSize[1] * camera.zoom)),
                    screenPos)

