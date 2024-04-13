import pygame

from mapObj import Map
import pygame as pg
from cameraObj import Camera
from src.StatusBar import StatusBar
from src.ui.UIManager import UIManager
from textureatlas import TextureAtlas
from entity.Entity import Entity
from ui.Inventory import Inventory

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
    healthbar = StatusBar((20, 10), (300, 20), 100, (9, 77, 5), (143, 13, 13))
    hungerbar = StatusBar((20, 40), (300, 20), 100, (191, 83, 6), (56, 55, 50))
    thirstbar = StatusBar((20, 70), (300, 20), 100, (40, 71, 156), (56, 55, 50))

    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")
    MainCamera = Camera((0, 0))
    testEn = Entity("asset/atlas.png")
    clock = pg.time.Clock()

    ui_manager = UIManager(WINDOW_SIZE)

    inventory = Inventory(3, 5, inventory_tile=texture_atlas.get_sprite((4, 0)))

    ui_manager.add_panel(inventory)

    # Main loop
    while running:
        delta_time = clock.tick(FPS) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_e:
                    ui_manager.toggle_active(inventory)

        # Deplete health when hunger or thirst status bars are at 0
        # TODO: make it so attacking deplete hunger
        # TODO: make it so walking deplete thirst
        if hungerbar.value <= 0:
            hungerbar.value = 0
        else:
            hungerbar.value -= .02

        if thirstbar.value <= 0:
            thirstbar.value = 0
        else:
            thirstbar.value -= .03

        if hungerbar.value == 0 or thirstbar.value == 0:
            healthbar.value -= .5

        MainSurface.fill((0, 0, 0))

        MainCamera.position = (testEn.position[0] + 50, testEn.position[1] + 50)

        MainMap.render_self(MainSurface, MainCamera)

        testEn.render_self(MainSurface, MainCamera)
        healthbar.render_self(MainSurface)
        hungerbar.render_self(MainSurface)
        thirstbar.render_self(MainSurface)

        ui_manager.render_self(MainSurface)

        pg.display.flip()



if __name__ == '__main__':
    main()