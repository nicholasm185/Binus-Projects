import sys
import pygame
from bullet import Bullet

def check_events(setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event, setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup(event,ship)

def keydown(event, setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_UP:
        ship.movingUp = True
    elif event.key == pygame.K_DOWN:
        ship.movingDown = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)

def keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
    elif event.key == pygame.K_UP:
        ship.movingUp = False
    elif event.key == pygame.K_DOWN:
        ship.movingDown = False

def update_screen(setting, screen, ship, bullets):
    screen.fill(setting.bg_color)
    ship.blipme()
    for bullet in bullets.sprites():
        bullet.drawBullet()
    pygame.display.flip()

