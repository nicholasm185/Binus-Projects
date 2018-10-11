class GameStats():

    def __init__(self, setting):
        self.setting = setting
        self.resetStats()
        self.gameActive = False

        self.highScore = 0

        self.level = 1


    def resetStats(self):
        self.shipsLeft = self.setting.shipLimit

        self.score = 0
        self.level = 1
