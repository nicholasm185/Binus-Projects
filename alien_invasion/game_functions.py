import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from bigBullet import bigBullet

def check_events(setting, screen, ship, bullets, bigbullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event, setting, screen, ship, bullets, bigbullets)
        elif event.type == pygame.KEYUP:
            keyup(event,ship)

def keydown(event, setting, screen, ship, bullets, bigbullets):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_UP:
        ship.movingUp = True
    elif event.key == pygame.K_DOWN:
        ship.movingDown = True
    elif event.key == pygame.K_q:
        sys.exit()

    if len(bullets) < setting.bulletAllowed:
        if event.key == pygame.K_SPACE:
            fireBullets(setting, screen, ship, bullets)
            effect = pygame.mixer.Sound(".\\images\\yeefx.wav")
            effect.play()

    if len(bigbullets) < setting.bigbulletAllowed:
        if event.key == pygame.K_m:
            firebigBullet(setting, screen, ship, bigbullets)
            bigeffect = pygame.mixer.Sound(".\\images\\oof.wav")
            bigeffect.play()


def keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
    elif event.key == pygame.K_UP:
        ship.movingUp = False
    elif event.key == pygame.K_DOWN:
        ship.movingDown = False

def update_screen(setting, screen, ship, aliens, bullets, bigbullets ):
    screen.fill(setting.bg_color)
    ship.blipme()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.drawBullet()
    for bigbullet in bigbullets:
        bigbullet.drawBullet()

    pygame.display.flip()

def updateBullets(settings, screen, ship, aliens, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    checkBulletAlienCollisions(settings, screen, ship, aliens, bullets)

def checkBulletAlienCollisions(settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    bullets.update()

    if len(aliens) == 0:
        bullets.empty()
        createFleet(settings, screen, ship, aliens)

def fireBullets(setting, screen, ship, bullets):
    new_bullet = Bullet(setting, screen, ship)
    bullets.add(new_bullet)

def createFleet(setting, screen, ship, aliens):
    alien = Alien(setting, screen)
    numberAliensX = getNumberAliensX(setting, alien.rect.width)
    numberRows = getNumberRows(setting, ship.rect.height, alien.rect.height)
    for rowNumber in range(numberRows):
        for alienNumber in range(numberAliensX):
            createAlien(setting, screen, aliens, alienNumber, rowNumber)

def getNumberAliensX(setting, alienWidth):
    availableSpaceX = setting.screenWidth - 2 * alienWidth
    numberAliensX = int(availableSpaceX/(2*alienWidth))
    return numberAliensX

def createAlien(setting, screen, aliens, alienNumber, rowNumber):
    alien = Alien(setting, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2 * alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    aliens.add(alien)

def updateAliens(settings, stats, screen, ship, aliens, bullets):
    checkFleetEdges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(settings, stats, screen, ship, aliens, bullets)

    checkAliensBottom(settings, stats, screen, ship, aliens, bullets)

def getNumberRows(setting, shipHeight, alienHeight):
    availableSpaceY = (setting.screenHeight - 3 * alienHeight - shipHeight)
    numberRows = int(availableSpaceY/(2 * alienHeight))
    return numberRows

def checkFleetEdges(setting, aliens):
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(setting, aliens)
            break

def changeFleetDirection(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.alienDropSpeed
    settings.alienDirection *= -1

def shipHit(setting, stats, screen, ship, aliens, bullets):
    if stats.shipsLeft > 0:
        stats.shipsLeft -= 1

        aliens.empty()
        bullets.empty()

        createFleet(setting, screen, ship, aliens)
        ship.centerShip()

        sleep(1)
    else:
        stats.gameActive = False

def checkAliensBottom(setting, stats, screen, ship, aliens, bullets):
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            shipHit(setting, stats, screen, ship, aliens, bullets)
            break

def updatebigBullets(settings, screen, ship, aliens, bigbullets):
    for bullet in bigbullets.copy():
        if bullet.rect.bottom <= 0:
            bigbullets.remove(bullet)

    checkbigBulletAlienCollisions(settings, screen, ship, aliens, bigbullets)

def checkbigBulletAlienCollisions(settings, screen, ship, aliens, bigbullets):
    collisions = pygame.sprite.groupcollide(bigbullets, aliens, False, True)
    bigbullets.update()

    if len(aliens) == 0:
        bigbullets.empty()
        createFleet(settings, screen, ship, aliens)

def firebigBullet(setting, screen, ship, bigbullets):
    new_bullet = bigBullet(setting, screen, ship)
    bigbullets.add(new_bullet)
