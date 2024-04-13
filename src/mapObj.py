import pygame
import pygame as pg
from cameraObj import Camera
class Map():


    def __init__(self, pos: tuple[float, float], texturePath: str):
        self.position = pos
        self.surfaceTexture = pygame.image.load(texturePath).convert()

    def render_self(self, screen: pg.Surface, camera: Camera):
        screenPos = camera.convertWorldToScreen(self.position, screen)
        mapSize = self.surfaceTexture.get_size()
        screen.blit(pg.transform.scale(self.surfaceTexture,(mapSize[0] * camera.zoom,mapSize[1] * camera.zoom)), screenPos)

