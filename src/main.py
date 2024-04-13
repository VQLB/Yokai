import pygame

from mapObj import Map
import pygame as pg
from cameraObj import Camera
from src.StatusBar import StatusBar
from src.ui.UIManager import UIManager
from textureatlas import TextureAtlas
from ui.Inventory import Inventory
from entity.Character import Character
from startscreen import StartScreen
from endscreen import EndScreen
from collider import collider

FPS = 60
WINDOW_SIZE = (800, 600)

def main():
    # Initialization
    running = True
    pg.init()
    MainSurface = pg.display.set_mode(WINDOW_SIZE)
    pg.display.set_caption('Yokai')

    # start screen button
    startscreen = StartScreen()


    texture_atlas = TextureAtlas("asset/atlas.png")

    # Status Bars
    healthbar = StatusBar((20, 10), (300, 20), 100, (9, 77, 5), (143, 13, 13))
    hungerbar = StatusBar((20, 40), (300, 20), 100, (191, 83, 6), (56, 55, 50))
    thirstbar = StatusBar((20, 70), (300, 20), 100, (40, 71, 156), (56, 55, 50))

    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")
    MainCamera = Camera((0, 0))
    MainCharacter = Character("asset/atlas.png")
    clock = pg.time.Clock()
    # BoundingBoxes
    leftWall = collider((-50,0),(50,1000))

    # inventory
    ui_manager = UIManager(WINDOW_SIZE)
    inventory = Inventory(3, 5, inventory_tile=texture_atlas.get_sprite((4, 0)))
    ui_manager.add_panel(inventory)


    # Main loop
    while running:
        delta_time = clock.tick(FPS) / 1000.0

        # if start screen visible, skip everything--else play everything else
        if startscreen.active:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    startscreen.active = False
            startscreen.render_self(MainSurface)

        else:
            keys = pygame.key.get_pressed()
            mainCharVec = [0,0]
            if keys[pg.K_w]:
                mainCharVec[1]+=-1
            if keys[pg.K_s]:
                mainCharVec[1] += 1
            if keys[pg.K_a]:
                mainCharVec[0] +=-1
            if keys[pg.K_d]:
                mainCharVec[0] +=1

            if (mainCharVec[0]!=0 or mainCharVec[1]!=0):
                if hungerbar.value <= 0:
                    hungerbar.value = 0
                else:
                    hungerbar.value -= .02

                if thirstbar.value <= 0:
                    thirstbar.value = 0
                else:
                    thirstbar.value -= .03

            MainCharacter.moveDir(tuple(mainCharVec), delta_time)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pygame.MOUSEWHEEL:
                    MainCamera.zoom+=event.y*0.01
                    MainCamera.zoom = max(0.25,min(MainCamera.zoom,2))
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_e:
                        ui_manager.toggle_active(inventory)

            MainSurface.fill((0, 0, 0))

            MainCamera.position = (MainCharacter.position[0] + 50, MainCharacter.position[1] + 50)

            MainMap.render_self(MainSurface, MainCamera)
            MainCharacter.render_self(MainSurface, MainCamera)
            healthbar.render_self(MainSurface)
            hungerbar.render_self(MainSurface)
            thirstbar.render_self(MainSurface)
            ui_manager.render_self(MainSurface)
            print(MainCharacter.isCollidingWith(leftWall))
            MainCharacter.resolveCollision(leftWall)
            MainCharacter.render_self(MainSurface, MainCamera)

            leftWall.render_self(MainSurface, MainCamera)

        pg.display.flip()

if __name__ == '__main__':
    main()