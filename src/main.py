import pygame

from mapObj import Map
import pygame as pg
from cameraObj import Camera
from textureatlas import TextureAtlas
from entity.Entity import Entity
from hungerbar import HungerBar
from thirstbar import ThirstBar
from healthbar import HealthBar

FPS = 60

def main():
    # Initialization
    running = True
    pg.init()
    MainSurface = pg.display.set_mode((800, 600), pygame.RESIZABLE)
    pg.display.set_caption('Yokai')
    # Status Bars
    healthbar = HealthBar(20, 10, 300, 20, 100)
    hungerbar = HungerBar(20, 40, 300, 20, 100)
    thirstbar = ThirstBar (20, 70, 300, 20, 100)

    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")
    MainCamera = Camera((0, 0))
    testEn = Entity("asset/atlas.png")
    clock = pg.time.Clock()

    texture_atlas = TextureAtlas("asset/atlas.png")

    # Main loop
    while running:
        delta_time = clock.tick(FPS) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        healthbar.health -= .01
        hungerbar.hunger -= .002
        thirstbar.thirst -= .002
        MainSurface.fill((0, 0, 0))

        MainCamera.position = (testEn.position[0] + 50, testEn.position[1] + 50)

        MainMap.render_self(MainSurface, MainCamera)
        testEn.render_self(MainSurface, MainCamera)
        healthbar.render_self(MainSurface)
        hungerbar.render_self(MainSurface)
        thirstbar.render_self(MainSurface)
        pg.display.flip()



if __name__ == '__main__':
    main()