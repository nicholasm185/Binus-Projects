import pygame
from pygame.sprite import Group
from settings import Settings
from ship import SpaceShip
import game_functions as gf
from bullet import Bullet

def runGame():
    pygame.init()
    gsett = Settings()
    screen = pygame.display.set_mode((gsett.screenHeight, gsett.screenWidth))
    pygame.display.set_caption("IS ALIEN INVASION")

    ship = SpaceShip(gsett.shipSpeed, screen)
    bullets = Group()

    while True:
        gf.check_events(gsett, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(gsett, screen, ship, bullets)


runGame()
