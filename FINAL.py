from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

black = Color(0, 1)
thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
noline = LineStyle(0, black)
cf = RectangleAsset(20, 30, thinline, gray)
laser = RectangleAsset(5, 10, noline, white)
class MC(Sprite):
    """
    Animated space ship
    """
    

    def __init__(self, position):
        super().__init__(cf, position)
        SpaceGame.listenKeyEvent("keydown", "d", self.dKey)
        SpaceGame.listenKeyEvent("keydown", "a", self.aKey)
        SpaceGame.listenKeyEvent("keydown", "s", self.sKey)
        SpaceGame.listenKeyEvent("keydown", "w", self.wKey)
        SpaceGame.listenKeyEvent("keydown", "e", self.eKey)
        SpaceGame.listenKeyEvent("keydown", "q", self.qKey)
        self.fxcenter = self.fycenter = 0.5
        print(self.fxcenter)
    def dKey(self, event):
        self.x += 1
    def aKey(self, event):
        self.x -= 1
    def wKey(self, event):
        self.y -= 1
    def sKey(self, event):
        self.y += 1
    def eKey(self, event):
        self.rotation += 1
    def qKey(self, event):
        self.rotation -= 1



class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
MC((320,240))
myapp.run()