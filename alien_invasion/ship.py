import pygame
from pygame.sprite import Sprite

class SpaceShip(Sprite):

    def __init__(self, settings, screen):
        super(SpaceShip, self).__init__()
        self.screen = screen
        self.speedSet = settings

        self.image = pygame.image.load(".\\images\\Untitled.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.movingRight = False
        self.movingLeft = False
        self.movingUp = False
        self.movingDown = False

    def update(self):
        if self.movingRight and self.centerx < self.screen_rect.right:
            self.centerx += self.speedSet
        elif self.movingLeft and self.centerx > 0:
            self.centerx -= self.speedSet
        elif self.movingUp and self.centery > 0:
            self.centery -= self.speedSet
        elif self.movingDown and self.centery < self.screen_rect.bottom:
            self.centery += self.speedSet

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def centerShip(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - self.rect.height/2

    def blipme(self):
        self.screen.blit(self.image, self.rect)
