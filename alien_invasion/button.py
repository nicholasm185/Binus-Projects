import pygame.font

class Button():

    def __init__(self, setting, screen, msg):
        self.screen = screen
        self.screenRect = screen.get_rect()

        self.width, self.height = 600, 50
        self.buttonColor = (0, 255, 0)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont("AR DECODE", 48)

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screenRect.center

        self.prepMSG(msg)

    def prepMSG(self, msg):
        self.msgImage = self.font.render(msg, True, self.textColor, self.buttonColor)
        self.msgImage_rect = self.msgImage.get_rect()
        self.msgImage_rect.center = self.rect.center

    def drawButton(self):
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage, self.msgImage_rect)
