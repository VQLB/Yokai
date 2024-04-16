import pygame
from src.cameraObj import Camera
from src.textureatlas import TextureAtlas
import pygame as pg
from uuid import UUID
import uuid
import math
from src.collider import collider

class Entity:
    def __init__(self, texture_atlas: TextureAtlas, textures: dict[str, tuple[int, int] | list[tuple[int, int]]], initial_texture: str, id: UUID | None = None):
        if not id:
            id = uuid.uuid4()
        self.id = id
        self.texture_atlas = texture_atlas
        self.textures = textures
        self.position = list((0, 0))
        self.collidable = True
        self.health = 100
        self.displayName = "Entity"
        self.speed = 100

        self.current_texture = initial_texture
        self.animation_frame = 0

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
            xRight = (self.position[0] + 100) - colliderObj.position[0]

            yUp = self.position[1] - (colliderObj.position[1] + colliderObj.size[1])
            yDown = (self.position[1] + 100) - colliderObj.position[1]

            if (min(abs(yUp), abs(yDown))<min(abs(xLeft), abs(xRight))):
                if (abs(yUp) < abs(yDown)):
                    self.position[1] += min(abs(yUp), abs(yDown)) * 1
                else:
                    self.position[1] -= min(abs(yUp), abs(yDown)) * 1
            else:
                if (abs(xLeft)<abs(xRight)):
                    self.position[0]+=min(abs(xLeft), abs(xRight))*1
                else:
                    self.position[0]-=min(abs(xLeft), abs(xRight)) * 1


            #print(min(abs(xLeft), abs(xRight)), abs(xLeft)<abs(xRight))


    def moveDir(self, vecDir: tuple[float, float], deltaTime: float):
        length = math.sqrt(vecDir[0]*vecDir[0] + vecDir[1]*vecDir[1])
        if length>0:
            normalizedVec = (vecDir[0]/length, vecDir[1]/length)
            self.position[0] += normalizedVec[0] * self.speed * max(0.0001,deltaTime)
            self.position[1] += normalizedVec[1] * self.speed * max(0.0001,deltaTime)

    def render_self(self, screen: pygame.Surface, camera: Camera):
        texture = self.textures[self.current_texture]
        if isinstance(texture, list):
            frame_idx = (self.animation_frame // 10) % len(texture)
            frame = texture[frame_idx]
        else:
            frame = texture
        #print('frame', frame)
        TextureSur = self.texture_atlas.get_sprite(frame)
        screenPos = camera.convertWorldToScreen(self.position, screen)
        mapSize = TextureSur.get_size()
        screen.blit(pg.transform.scale(TextureSur, (mapSize[0] * camera.zoom, mapSize[1] * camera.zoom)),
                    screenPos)

