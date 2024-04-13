import pygame
import pygame as pg
from cameraObj import Camera
class Map():


    def __init__(self, pos: tuple[float, float], texturePath: str):
        self.position = pos
        self.surfaceTexture = pygame.image.load(texturePath).convert()

    def render_self(self, screen: pg.Surface, camera: Camera):
        screenPos = camera.convertWorldToScreen(self.position, screen)
        screen.blit(self.surfaceTexture, screenPos)

