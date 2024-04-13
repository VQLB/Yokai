from mapObj import Map
import pygame as pg
from cameraObj import Camera
from src.ui.UIManager import UIManager
from textureatlas import TextureAtlas
from hungerbar import HungerBar
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
    # Bars
    bar = HungerBar(20, 10, 300, 20, 100)
    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")
    MainCamera = Camera((500, 500))
    clock = pg.time.Clock()

    ui_manager = UIManager(WINDOW_SIZE)

    inventory = Inventory(3, 5, inventory_tile=texture_atlas.get_sprite((4, 0)))

    ui_manager.add_panel(inventory)
    ui_manager.make_active(inventory)

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

        ui_manager.render_self(MainSurface)

        pg.display.flip()



if __name__ == '__main__':
    main()