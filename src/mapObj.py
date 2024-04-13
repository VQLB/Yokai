import pygame as pg

class Map():
    posX = 0
    posY = 0


    def __init__(self, posX: float, posY: float, texturePath: str):
        self.posX = posX
        self.posY = posY

    def render_self(self, screen: pg.Surface):
        screen.
