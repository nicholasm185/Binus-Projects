import pygame
from pygame.sprite import Group
from settings import Settings
from ship import SpaceShip
from gamestats import GameStats
import game_functions as gf

def runGame():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screenWidth, setting.screenHeight))
    pygame.display.set_caption("IS ALIEN INVASION")

    stats = GameStats(setting)
    ship = SpaceShip(setting.shipSpeed, screen)

    bigbullets = Group()
    bullets = Group()
    aliens = Group()

    gf.createFleet(setting, screen, ship, aliens)

    pygame.mixer.music.load(".\\images\\Yee.mp3")
    pygame.mixer.music.play(-1)

    while True:
        gf.check_events(setting, screen, ship, bullets, bigbullets)

        if stats.gameActive:
            ship.update()
            gf.updateBullets(setting, screen, ship, aliens, bullets)
            gf.updatebigBullets(setting,screen,ship,aliens,bigbullets)
            gf.updateAliens(setting, stats, screen, ship, aliens, bullets)

        gf.update_screen(setting, screen, ship, aliens, bullets, bigbullets)


runGame()
