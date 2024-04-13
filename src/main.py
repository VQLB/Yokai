from mapObj import Map
import pygame as pg
from cameraObj import Camera

def main():
    # Initialization
    running = True
    pg.init()
    MainSurface = pg.display.set_mode((800, 600))
    pg.display.set_caption('Yokai')

    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")
    MainCamera = Camera((500,500))
    # Main loop
    while running:
        MainCamera.zoom -=0.001
        MainCamera.position[0]+=0.1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        MainSurface.fill((0, 0, 0))

        MainMap.render_self(MainSurface, MainCamera)

        pg.display.flip()



if __name__ == '__main__':
    main()