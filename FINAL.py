from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from math import sin, cos, radians, pi


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xf8f8ff, 1.0)
pwhite = Color(0xfffafa,1.0) 
thinline = LineStyle(1, black)
thinline1 = LineStyle(1, pwhite)
noline = LineStyle(0, black)
roof = PolygonAsset([(0,0), (200,0), (100, -120)], thinline, black)
cf = RectangleAsset(20, 30, thinline, gray)
laser = RectangleAsset(5, 10, noline, pwhite)
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
        self.xvector = cos(self.rotation)
        self.yvector = sin(self.rotation)
    def dKey(self, event):
        self.x += cos(self.rotation)
        self.y -= sin(self.rotation)
    def aKey(self, event):
        self.x -= cos(self.rotation)
        self.y += sin(self.rotation)
    def wKey(self, event):
        self.x -= cos((pi/2)-self.rotation)
        self.y -= sin((pi/2)-self.rotation)
    def sKey(self, event):
        self.x += cos((pi/2)-self.rotation)
        self.y += sin((pi/2)-self.rotation)
    def eKey(self, event):
        self.rotation += .09
    def qKey(self, event):
        self.rotation -= .09


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