class Settings:

    def __init__(self):
        self.screenWidth = 1000
        self.screenHeight = 500
        self.bg_color = (0, 127, 255)
        # self.bg_color = (255, 255, 255)

        self.shipSpeed = 0.75
        self.shipLimit = 3

        self.bulletSpeed = 1
        self.bigbulletSpeed = 1.5
        self.bulletWidth = 200
        self.bulletHeight = 20
        self.bulletColor = (255, 0, 0)
        self.bulletAllowed = 10
        self.bigbulletAllowed = 1

        self.alienSpeed = 0.5
        self.alienDirection = 1
        self.alienDropSpeed = 10
