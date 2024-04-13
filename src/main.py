from mapObj import Map
import pygame as pg
from cameraObj import Camera
from textureatlas import TextureAtlas
from entity.Entity import Entity

def main():
    # Initialization
    running = True
    pg.init()
    MainSurface = pg.display.set_mode((800, 600))
    pg.display.set_caption('Yokai')

    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")
    MainCamera = Camera((0, 0))
    testEn = Entity("asset/testCharacter.png")

    texture_atlas = TextureAtlas("asset/atlas.png")

    # Main loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        MainSurface.fill((0, 0, 0))

        MainMap.render_self(MainSurface, MainCamera)
        testEn.render_self(MainSurface, MainCamera)

        pg.display.flip()



if __name__ == '__main__':
    main()