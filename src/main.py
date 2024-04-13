from mapObj import mapObj
import pygame as pg
def main():
    running = True
    pg.init()
    mainDisplay = pg.display.set_mode((800, 600))
    pg.display.set_caption('Yokai')
    #main loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        mainDisplay.fill((255, 255, 255))
        pg.display.flip()

if __name__ == '__main__':
    main()