import pygame
import pygame as pg
from cameraObj import Camera
class Map():


    def __init__(self, pos: tuple[float, float], texturePath: str):
        self.posX = pos[0]
        self.posY = pos[1]
        self.surfaceTexture = pygame.image.load(texturePath).convert()

    def render_self(self, screen: pg.Surface, camera: Camera):
        textureSize = self.surfaceTexture.get_size()
        screen.blit(pygame.transform.scale(self.surfaceTexture, (100,100)), (self.posX + camera.posY, self.posY + camera.posX))

