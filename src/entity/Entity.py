import pygame
from src.cameraObj import Camera
from src.textureatlas import TextureAtlas
import pygame as pg
from uuid import UUID
import uuid
import math

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
        self.speed = 1

        self.current_texture = initial_texture
        self.animation_frame = 0

    def modifyHealth(self, offset):
        self.health += offset

    def moveDir(self, vecDir: tuple[float, float]):
        length = math.sqrt(vecDir[0]*vecDir[0] + vecDir[1]*vecDir[1])
        if length>0:
            normalizedVec = (vecDir[0]/length, vecDir[1]/length)
            self.position[0] += normalizedVec[0] * self.speed
            self.position[1] += normalizedVec[1] * self.speed

    def render_self(self, screen: pygame.Surface, camera: Camera):
        texture = self.textures[self.current_texture]
        if isinstance(texture, list):
            frame_idx = (self.animation_frame // 10) % len(texture)
            frame = texture[frame_idx]
        else:
            frame = texture
        print('frame', frame)
        TextureSur = self.texture_atlas.get_sprite(frame)
        screenPos = camera.convertWorldToScreen(self.position, screen)
        mapSize = TextureSur.get_size()
        screen.blit(pg.transform.scale(TextureSur, (mapSize[0] * camera.zoom, mapSize[1] * camera.zoom)),
                    screenPos)

