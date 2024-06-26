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
from entity.Enemy import Enemy
from collider import collider
from entity.FoodObj import FoodObj
import random
import math
random.seed(69)
FPS = 60
DRAW_BOUND = False
WINDOW_SIZE = (800, 600)
MaxMonster = 3

def spawnEnemy(EnemyList, texture_atlas, MainChar):
    EnemyList.append(Enemy(texture_atlas,
                           {
                               'move_left': [(3, 0),(3,1)],
                               'move_right': [(2,2),(2,3)],
                               'hurt': [(7,1),(7,2)]
                           },
                           'move_left'
                           ))
    EnemyList[len(EnemyList) - 1].speed = 40
    spawnPos = list((random.randint(50,950), random.randint(50,950)))
    while math.sqrt(math.pow(spawnPos[0]-MainChar.position[0],2)+math.pow(spawnPos[1]-MainChar.position[1],2))<400:
        spawnPos = list((random.randint(50, 950), random.randint(50, 950)))
    EnemyList[len(EnemyList) - 1].position = spawnPos

def spawnFood(PickupList, texture_atlas, pos: list[int, int]):
    PickupList.append(FoodObj(texture_atlas,
                           {
                               'default' : [(4,3)]
                           },
                           'default'
                           ))
    PickupList[len(PickupList) - 1].position = pos
    PickupList[len(PickupList) - 1].speed = 200

def main():
    # Initialization
    currentScreen = "start"
    running = True
    deathCoolDown = 60
    pickupEntities = []
    pg.init()
    pg.mixer.init()
    background = pg.mixer.Sound('sound/background music.mp3')
    laugh = pg.mixer.Sound('sound/yokai laugh.mp3')
    background.play(loops=-1)
    pg.mixer.music.set_volume(0.2)
    laugh.set_volume(0.4)
    MainSurface = pg.display.set_mode(WINDOW_SIZE)
    pg.display.set_caption('Yokai')

    # Start and End Screen
    startscreen = StartScreen()
    endscreen = EndScreen()
    texture_atlas = TextureAtlas("asset/atlas.png")

    # Status Bars
    healthbar = StatusBar((20, 10), (300, 20), 100, (9, 77, 5), (143, 13, 13))
    hungerbar = StatusBar((20, 40), (300, 20), 100, (191, 83, 6), (56, 55, 50))
    thirstbar = StatusBar((20, 70), (300, 20), 100, (40, 71, 156), (56, 55, 50))

    # Main obj init
    MainMap = Map((0, 0), "asset/map.png")

    MainCamera = Camera((0, 0))
    MainCamera.zoom = 1.2
    # MainCharacter
    # in textures:
    # for a still frame just put (x, y)
    # for animated frames put [(x, y), (x2, y2), ...]
    MainCharacter = Character(
        texture_atlas,
        {
            'still_left': (0, 0),
            'still_right': (1, 0),
            'still_down': (0, 3),
            'move_left': [(0, 1), (1, 1), (2, 1), (1, 1)],
            'move_right': [(0, 2), (6,2), (1, 0) ,(1, 2),(6,2) ,(1, 0)],
            'move_down': [(0, 3), (1, 3)],
            'move_up': [(7,0), (6,3)],
            'attack': [(3,2),(3,3),(4,0),(4,1)]
        },
        'still_right'
    )
    MainCharacter.position = [100,100]
    MainCharAttackFrameCount=0
    # Enemy
    EnemyList: [Enemy, ...] = []
    for i in range(1):
        spawnEnemy(EnemyList, texture_atlas, MainCharacter)

    clock = pg.time.Clock()
    # BoundingBoxes
    leftWall = collider((0,0),(50,1000))
    topWall = collider((0,50),(1000,50))
    bottomWall = collider((-50,950),(1000,50))
    rightWall = collider((950,0),(50,1000))
    bigLakeBound = collider((420,170),(420,50))
    bigLakeDrink = collider((370,120),(520,150))
    smallLakeBound = collider((170,820),(200,30))
    smallLakeDrink = collider((120, 790), (300, 90))
    attackBound = collider((0,0), (100, 150))
    hurtBound = collider((0,0),(25,50))

    # inventory
    ui_manager = UIManager(WINDOW_SIZE)

    inventory = Inventory(3, 5, inventory_tile=texture_atlas.get_sprite((2, 0)))

    ui_manager.add_panel(inventory)


    # Main loop
    while running:
        MainSurface.fill((0, 0, 0))
        delta_time = clock.tick(FPS) / 1000.0

        # if start screen visible, skip everything--else play everything else
        if currentScreen == "start":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    startscreen.active = False
                    currentScreen = "game"
            startscreen.render_self(MainSurface)
        elif currentScreen == "end":
            deathCoolDown -= 1
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN and deathCoolDown<=0:
                    if pygame.mouse.get_pressed()[0]:
                        currentScreen = "game"
                        MainCharacter.health = 100
                        MainCharacter.hunger = 100
                        hungerbar.value = MainCharacter.hunger
                        thirstbar.value = 100
                        EnemyList = []
                        pickupEntities = []
                        MainCharacter.position = [100,100]
                        for i in range(MaxMonster):
                            spawnEnemy(EnemyList, texture_atlas, MainCharacter)

            MainSurface.blit(pygame.image.load('asset/ending_screen.png'), (0, 0))
        elif currentScreen == "game":
            keys = pygame.key.get_pressed()
            main_character_vector = [0.0, 0.0]
            if keys[pg.K_w]:
                main_character_vector[1] += -1.5
            if keys[pg.K_s]:
                main_character_vector[1] += 1.5
            if keys[pg.K_a]:
                main_character_vector[0] += -1.5
            if keys[pg.K_d]:
                main_character_vector[0] += 1.5
            if MainCharacter.current_texture != "attack":
                if main_character_vector[0] < 0:
                    MainCharacter.current_texture = 'move_left'

                elif main_character_vector[0] > 0:
                    MainCharacter.current_texture = 'move_right'

                elif main_character_vector[0] == 0:
                    if MainCharacter.current_texture == 'move_left':
                        MainCharacter.current_texture = 'still_left'
                    elif MainCharacter.current_texture == 'move_right':
                        MainCharacter.current_texture = 'still_right'
                    elif MainCharacter.current_texture == 'move_down':
                        MainCharacter.current_texture = 'still_down'

                if main_character_vector[1] > 0 and main_character_vector[0] == 0:
                    MainCharacter.current_texture = 'move_down'
                elif main_character_vector[1] < 0:
                    MainCharacter.current_texture = "move_up"
                    if MainCharacter.current_texture == 'still_left':
                        MainCharacter.current_texture = 'move_left'
                    elif MainCharacter.current_texture == 'still_right':
                        MainCharacter.current_texture = 'move_right'
            else:
                MainCharAttackFrameCount-=1
                if MainCharAttackFrameCount<=0:
                    MainCharacter.current_texture="still_right"
            MainCharacter.animation_frame += 1

            if main_character_vector[0] != 0 or main_character_vector[1] != 0:
                if thirstbar.value <= 0:
                    thirstbar.value = 0
                else:
                    thirstbar.value -= .02
                if MainCharacter.hunger <= 0:
                    MainCharacter.hunger = 0
            MainCharacter.moveDir(tuple(main_character_vector), delta_time)

            # Health bar depletes when one of the status bars are gone
            healthbar.value = MainCharacter.health
            if MainCharacter.hunger == 0 or thirstbar.value == 0:
                MainCharacter.health -= .05
            if MainCharacter.health <= 0:
                print("ending")
                currentScreen = "end"
                deathCoolDown=60
            # zoom in feature for debugging
            # EVENT HANDLING
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pygame.MOUSEWHEEL:
                    MainCamera.zoom+=event.y*0.01
                    print("a")
                    MainCamera.zoom = max(1.15,min(MainCamera.zoom,1.25))
                    print(MainCamera.zoom)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_e:
                        ui_manager.toggle_active(inventory)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if MainCharAttackFrameCount<=0:
                            print("left click")
                            MainCharacter.current_texture = "attack"
                            MainCharAttackFrameCount = 60
                            for i in EnemyList:
                                if i.isCollidingWith(attackBound):
                                    laugh.play()
                                    i.health -= 35
                                    i.hurtFreezeTimer = 40
                                if i.health<=0 and random.randint(1,10)<=7:
                                    spawnFood(pickupEntities, texture_atlas, i.position)
                            EnemyList = [i for i in EnemyList if not i.health<0]
                            MainCharacter.hunger-=2
                            if (len(EnemyList)<MaxMonster):
                                spawnEnemy(EnemyList, texture_atlas, MainCharacter)
            hungerbar.value = MainCharacter.hunger
            MainCharacter.resolveCollision(leftWall)
            MainCharacter.resolveCollision(topWall)
            MainCharacter.resolveCollision(bottomWall)
            MainCharacter.resolveCollision(rightWall)
            MainCharacter.resolveCollision(bigLakeBound)
            MainCharacter.resolveCollision(smallLakeBound)
            if MainCharacter.isCollidingWith(bigLakeDrink):
                thirstbar.value=min(100,thirstbar.value + 0.2)
            if MainCharacter.isCollidingWith(smallLakeDrink):
                thirstbar.value=min(100,thirstbar.value + 0.2)


            # Zoom bounding
            MainCamera.position = (min(max(MainCharacter.position[0] + 50, WINDOW_SIZE[0]/2/MainCamera.zoom), 1000-WINDOW_SIZE[0]/2/MainCamera.zoom), min(max(MainCharacter.position[1] + 50,WINDOW_SIZE[1]/2/MainCamera.zoom), 1000-WINDOW_SIZE[1]/2/MainCamera.zoom))
            # no bounding
            # MainCamera.position = (MainCharacter.position[0], MainCharacter.position[1])

            attackBound.position = (MainCharacter.position[0], MainCharacter.position[1] - 25)
            hurtBound.position = (MainCharacter.position[0] + 37.5, MainCharacter.position[1] + 25)

            MainMap.render_self(MainSurface, MainCamera)
            MainCharacter.render_self(MainSurface, MainCamera)

            for i in pickupEntities:
                i.render_self(MainSurface, MainCamera)
                i.moveTowardEntity(MainCharacter, delta_time)
            pickupEntities = [i for i in pickupEntities if not i.consumed]

            for i in EnemyList:
                i.moveTowardEntity(MainCharacter, delta_time)
                i.render_self(MainSurface, MainCamera)
                i.animation_frame += 1
                if i.isCollidingWith(hurtBound):
                    MainCharacter.health-=0.25

            healthbar.render_self(MainSurface)
            hungerbar.render_self(MainSurface)
            thirstbar.render_self(MainSurface)

            ui_manager.render_self(MainSurface)
            if DRAW_BOUND:
                topWall.render_self(MainSurface, MainCamera)
                leftWall.render_self(MainSurface, MainCamera)
                bottomWall.render_self(MainSurface, MainCamera)
                rightWall.render_self(MainSurface, MainCamera)
                bigLakeBound.render_self(MainSurface, MainCamera)
                bigLakeDrink.render_self(MainSurface, MainCamera)
                attackBound.render_self(MainSurface, MainCamera)
                hurtBound.render_self(MainSurface, MainCamera)
                smallLakeBound.render_self(MainSurface, MainCamera)
                smallLakeDrink.render_self(MainSurface, MainCamera)
                # UI must render on top of everything
                ui_manager.render_self(MainSurface)

        pg.display.flip()

if __name__ == '__main__':
    main()