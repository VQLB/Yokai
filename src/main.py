import pygame

from mapObj import Map
import pygame as pg
from cameraObj import Camera
from src.ui.UIManager import UIManager
from textureatlas import TextureAtlas
from entity.Entity import Entity
from hungerbar import HungerBar
from ui.Inventory import Inventory
from thirstbar import ThirstBar
from healthbar import HealthBar
from entity.Character import Character

FPS = 60
WINDOW_SIZE = (800, 600)

def main():
    # Initialization
    running = True
    pg.init()
    MainSurface = pg.display.set_mode(WINDOW_SIZE)
    pg.display.set_caption('Yokai')

    texture_atlas = TextureAtlas("asset/atlas.png")

    # Status Bars
    healthbar = HealthBar(20, 10, 300, 20, 100)
    hungerbar = HungerBar(20, 40, 300, 20, 100)
    thirstbar = ThirstBar (20, 70, 300, 20, 100)

    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")
    MainCamera = Camera((0, 0))
    MainCharacter = Character("asset/atlas.png")
    clock = pg.time.Clock()

    ui_manager = UIManager(WINDOW_SIZE)

    inventory = Inventory(3, 5, inventory_tile=texture_atlas.get_sprite((4, 0)))

    ui_manager.add_panel(inventory)

    # Main loop
    while running:
        delta_time = clock.tick(FPS) / 1000.0
        print(delta_time)

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

        MainCharacter.moveDir(tuple(mainCharVec))


        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                MainCamera.zoom+=event.y*0.01
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_e:
                    ui_manager.toggle_active(inventory)

        # Deplete health when hunger or thirst status bars are at 0
        # TODO: make it so attacking deplete hunger
        # TODO: make it so walking deplete thirst
        if hungerbar.hunger <= 0:
            hungerbar.hunger = 0
        else:
            hungerbar.hunger -= .02

        if thirstbar.thirst <= 0:
            thirstbar.thirst = 0
        else:
            thirstbar.thirst -= .03

        if hungerbar.hunger == 0 or thirstbar.thirst == 0:
            healthbar.health -= .5

        MainSurface.fill((0, 0, 0))

        MainCamera.position = (MainCharacter.position[0] + 50, MainCharacter.position[1] + 50)

        MainMap.render_self(MainSurface, MainCamera)
        MainCharacter.render_self(MainSurface, MainCamera)
        healthbar.render_self(MainSurface)
        hungerbar.render_self(MainSurface)
        thirstbar.render_self(MainSurface)
        ui_manager.render_self(MainSurface)
        pg.display.flip()



if __name__ == '__main__':
    main()