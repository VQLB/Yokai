from mapObj import Map
import pygame as pg
from cameraObj import Camera
from textureatlas import TextureAtlas
from hungerbar import HungerBar

FPS = 60

def main():
    # Initialization
    running = True
    pg.init()
    MainSurface = pg.display.set_mode((800, 600))
    pg.display.set_caption('Yokai')
    # Bars
    bar = HungerBar(20, 10, 300, 20, 100)
    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")
    MainCamera = Camera((500, 500))
    clock = pg.time.Clock()

    texture_atlas = TextureAtlas("asset/atlas.png")

    # Main loop
    while running:
        delta_time = clock.tick(FPS) / 1000.0

        MainCamera.position[0] += 0.1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        bar.hunger -= .002
        MainSurface.fill((0, 0, 0))

        MainMap.render_self(MainSurface, MainCamera)
        bar.render_self(MainSurface)
        pg.display.flip()



if __name__ == '__main__':
    main()