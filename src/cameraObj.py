import pygame
class Camera:
    def __init__(self, pos: tuple[float, float]):
        self.position = list(pos)
        self.zoom = 1

    def convertWorldToScreen(self, pos: tuple[float ,float], surface: pygame.surface) -> tuple[float, float]:
        returnPos = [0,0]
        screenSize = surface.get_size()
        returnPos[0] = (pos[0] - self.position[0]) * (self.zoom) + screenSize[0]/2
        returnPos[1] = (pos[1] - self.position[1]) * (self.zoom) + screenSize[1]/2
        return tuple(returnPos)