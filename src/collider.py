import pygame
import pygame as pg
from cameraObj import Camera
class collider():
    def __init__(self,pos: tuple[float, float], dimension: tuple[float, float]):
        self.position = list(pos)
        self.size = list(dimension)

    def render_self(self, screen: pg.Surface, camera: Camera):
        screenPos = camera.convertWorldToScreen(tuple(self.position), screen)
        pg.draw.rect(screen, (255,0,0), pygame.Rect(screenPos[0], screenPos[1],self.size[0] * camera.zoom, self.size[1] * camera.zoom), 2)