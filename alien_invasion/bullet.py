import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, setting, screen, ship):
        super(Bullet,self).__init__()
        self.screen = screen

        self.image = pygame.image.load(".\\images\\man.bmp")

        # self.rect = pygame.Rect(0, 0, setting.bulletWidth, setting.bulletHeight)
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = setting.bulletColor
        self.speed = setting.bulletSpeed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def drawBullet(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
