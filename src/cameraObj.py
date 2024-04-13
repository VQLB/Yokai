import pygame
class Camera:
    def __init__(self, pos: tuple[float, float]):
        self.position = pos
        self.zoom = 0

    def convertWorldToScreen(self, pos: tuple[float ,float], surface: pygame.surface) -> tuple[float, float]:
        returnPos = list(pos)
        screenSize = surface.get_size()
        returnPos[0] += self.position[0] + screenSize[0]/2
        returnPos[1] += self.position[1] + screenSize[1]/2
        print(returnPos)
        return tuple(returnPos)