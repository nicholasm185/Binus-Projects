import pygame.font
from pygame.sprite import Group

from ship import SpaceShip

class Scoreboard:

    def __init__(self, setting, screen, stats):
        self.screen = screen
        self.setting = setting
        self.stats = stats

        self.screenRect = screen.get_rect()

        self.txtColor = (30,30,30)
        self.font = pygame.font.SysFont("calibri", 20)

        self.prepScore()
        self.prepHighScore()
        self.prepLevel()
        self.prepShips()


    def prepShips(self):
        self.lives = Group()
        for shipNumber in range(self.stats.shipsLeft):
            ship = SpaceShip(self.setting, self.screen)
            ship.rect.x = 10 + shipNumber * ship.rect.width
            ship.rect.y = 10

            self.lives.add(ship)

    def prepLevel(self):
        self.levelImage = self.font.render(str(self.stats.level), True, self.txtColor, self.setting.bg_color)

        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.score_rect.right
        self.levelRect.top = self.score_rect.bottom + 10

    def prepHighScore(self):
        highScore = round(self.stats.highScore, -1)
        highScoreStr = "{:,}".format(highScore)
        self.highScoreImage = self.font.render(highScoreStr, True, self.txtColor, self.setting.bg_color)

        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.score_rect.top

    def prepScore(self):
        scoreStr = str(self.stats.score)
        roundedScore = round(self.stats.score, -1)
        scoreStr = "{:,}".format(roundedScore)
        self.scoreImage = self.font.render(scoreStr, True, self.txtColor, self.setting.bg_color)

        self.score_rect = self.scoreImage.get_rect()
        self.score_rect.right = self.screenRect.right - 40
        self.score_rect.top = 40

    def showScore(self):
        self.screen.blit(self.scoreImage, self.score_rect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.levelImage, self.levelRect)
        self.lives.draw(self.screen)
