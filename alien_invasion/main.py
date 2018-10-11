import pygame
from pygame.sprite import Group
from settings import Settings
from ship import SpaceShip
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def runGame():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screenWidth, setting.screenHeight))
    pygame.display.set_caption("IS ALIEN INVASION")
    playButton = Button(setting, screen, "PLAY")

    ship = SpaceShip(setting.shipSpeed, screen)
    stats = GameStats(setting)
    sb = Scoreboard(setting, screen, stats)

    bigbullets = Group()
    bullets = Group()
    aliens = Group()

    gf.createFleet(setting, screen, ship, aliens)

    pygame.mixer.music.load(".\\images\\Yee.mp3")

    while True:
        gf.check_events(setting, screen, stats, sb, playButton, ship, aliens, bullets, bigbullets)

        if stats.gameActive:
            ship.update()
            gf.updateBullets(setting, screen, stats, sb, ship, aliens, bullets)
            gf.updatebigBullets(setting, screen, stats, sb, ship, aliens, bigbullets)
            gf.increaseLevel(stats, sb, aliens)
            gf.updateAliens(setting, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(setting, screen, stats, sb, ship, aliens, bullets, bigbullets, playButton)


runGame()
