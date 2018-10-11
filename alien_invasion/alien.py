import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load(".\\images\\pup.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.setting.alienSpeed * self.setting.alienDirection)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def checkEdges(self):
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right:
            return True
        elif self.rect.left <= 0:
            return True
