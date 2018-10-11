import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from bigBullet import bigBullet


def check_events(setting, screen, stats, sb, playButton, ship, aliens, bullets, bigbullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown(event, setting, screen, ship, bullets, bigbullets)
        elif event.type == pygame.KEYUP:
            keyup(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            checkPlayButton(setting, screen, stats, sb, playButton, ship, aliens, bullets, bigbullets, mouse_x, mouse_y)


def checkPlayButton(setting, screen, stats, sb, playButton, ship, aliens, bullets, bigbullets, mouse_x, mouse_y):
    buttonClicked = playButton.rect.collidepoint(mouse_x,mouse_y)
    if buttonClicked and not stats.gameActive:
        if playButton.rect.collidepoint(mouse_x, mouse_y):

            pygame.mouse.set_visible(False)

            stats.resetStats()
            setting.initializeDynamicSettings()

            sb.prepScore()
            sb.prepHighScore()
            sb.prepLevel()
            sb.prepShips

            aliens.empty()
            bullets.empty()
            bigbullets.empty()

            createFleet(setting, screen, ship, aliens)
            ship.centerShip()

            pygame.mixer.music.play(-1)

            stats.gameActive = True


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
            bigeffect = pygame.mixer.Sound(".\\images\\succ.wav")
            bigeffect.set_volume(0.05)
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


def update_screen(setting, screen, stats, sb, ship, aliens, bullets, bigbullets, playButton):

    screen.fill(setting.bg_color)
    ship.blipme()
    aliens.draw(screen)
    sb.showScore()

    for bullet in bullets.sprites():
        bullet.drawBullet()
    for bigbullet in bigbullets:
        bigbullet.drawBullet()

    if not stats.gameActive:
        playButton.drawButton()

    pygame.display.flip()


def updateBullets(settings, screen, stats, sb, ship, aliens, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    checkBulletAlienCollisions(settings, screen, stats, ship, sb, aliens, bullets)


def checkBulletAlienCollisions(settings, screen, stats, ship, sb, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    bullets.update()

    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alienPoints * len(aliens)
            sb.prepScore()
        checkHighScore(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        createFleet(settings, screen, ship, aliens)
        settings.increaseSpeed()


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


def updateAliens(settings, stats, sb, screen, ship, aliens, bullets):
    checkFleetEdges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(settings, stats, sb, screen, ship, aliens, bullets)

    checkAliensBottom(settings, stats, sb, screen, ship, aliens, bullets)


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


def shipHit(setting, stats, sb, screen, ship, aliens, bullets):
    if stats.shipsLeft > 0:

        dieeffect = pygame.mixer.Sound(".\\images\\oof.wav")
        dieeffect.play()

        stats.shipsLeft -= 1

        sb.prepShips()

        aliens.empty()
        bullets.empty()

        createFleet(setting, screen, ship, aliens)
        ship.centerShip()

        sleep(1)
    else:
        stats.gameActive = False
        pygame.mixer.music.stop()
        pygame.mouse.set_visible(True)


def checkAliensBottom(setting, stats, sb, screen, ship, aliens, bullets):
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            shipHit(setting, stats, sb, screen, ship, aliens, bullets)
            break


def updatebigBullets(settings, screen, stats, sb, ship, aliens, bigbullets):
    for bullet in bigbullets.copy():
        if bullet.rect.bottom <= 0:
            bigbullets.remove(bullet)

    checkbigBulletAlienCollisions(settings, screen, stats, sb, ship, aliens, bigbullets)


def checkbigBulletAlienCollisions(settings, screen, stats, sb, ship, aliens, bigbullets):
    collisions = pygame.sprite.groupcollide(bigbullets, aliens, False, True)
    bigbullets.update()

    if collisions:
        for aliens in collisions.values():
            stats.score += int(settings.alienPoints/2) * len(aliens)
            sb.prepScore()
        checkHighScore(stats, sb)

    if len(aliens) == 0:
        bigbullets.empty()
        createFleet(settings, screen, ship, aliens)
        settings.increaseSpeed()



def firebigBullet(setting, screen, ship, bigbullets):
    new_bullet = bigBullet(setting, screen, ship)
    bigbullets.add(new_bullet)


def checkHighScore(stats, sb):
    if stats.score > stats.highScore:
        stats.highScore = stats.score
        sb.prepHighScore()

def increaseLevel(stats, sb, aliens):
    if len(aliens) <= 0:
        stats.level += 1
        sb.prepLevel()
