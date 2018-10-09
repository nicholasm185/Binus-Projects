class GameStats():

    def __init__(self, setting):
        self.setting = setting
        self.resetStats()
        self.gameActive = True

    def resetStats(self):
        self.shipsLeft = self.setting.shipLimit
