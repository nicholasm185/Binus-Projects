import pygame

class Settings:

    def __init__(self):
        self.screenWidth = 1000
        self.screenHeight = 500
        # self.bg_color = pygame.image.load(".\\images\\space.jpg")
        self.bg_color = (0, 127, 255)

        self.shipSpeed = 0.75
        self.shipLimit = 3

        self.bulletSpeed = 1
        self.bigbulletSpeed = 1.5
        self.bulletWidth = 500
        self.bulletHeight = 20
        self.bulletColor = (255, 0, 0)
        self.bulletAllowed = 10
        self.bigbulletAllowed = 1

        self.alienSpeed = 0.5
        self.alienDirection = 1
        self.alienDropSpeed = 10

        self.speedup = 1.5
        self.scoreScale = 1.5

        self.initializeDynamicSettings()

    def initializeDynamicSettings(self):
        self.shipSpeed = 1.5
        self.bulletSpeed = 3
        self.bigbulletSpeed = 5
        self.alienSpeed = 1
        self.alienDirection = 1
        self.alienPoints = 50

    def increaseSpeed(self):
        self.shipSpeed *= self.speedup
        self.bulletSpeed *= self.speedup
        self.alienSpeed *= self.speedup

        self.alienPoints = int(self.alienPoints * self.scoreScale)
