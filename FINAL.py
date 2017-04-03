from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from math import sin, cos, radians, pi


SCREEN_WIDTH1 = 640
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 2*SCREEN_WIDTH1
black = Color(0, 1)

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)


thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
noline = LineStyle(0, black)
thinline1 = LineStyle(1, white)
flashlight= PolygonAsset([(-SCREEN_WIDTH, SCREEN_WIDTH), (-SCREEN_WIDTH, -SCREEN_WIDTH), (SCREEN_WIDTH, -SCREEN_WIDTH), (SCREEN_WIDTH, SCREEN_WIDTH), (0, SCREEN_WIDTH), (0, -15), (20, -75), (-20, -75), (0,-15), (0, SCREEN_WIDTH)], noline, black)
Leftside = Sprite(flashlight, (320, 240))

cf = PolygonAsset(((-10,-15),(10,-15),(10,15),(-10,15)), thinline, gray)
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
        self.cornerx = [18.02*cos(pi/4-self.rotation), 18.02*cos((7*pi/4)-self.rotation), 18.02*cos((3*pi/4)-self.rotation), 18.02*cos(5*pi/4-self.rotation)]
        self.cornery = [18.02*sin(pi/4-self.rotation), 18.02*sin((7*pi/4)-self.rotation), 18.02*sin((3*pi/4)-self.rotation), 18.02*sin(5*pi/4-self.rotation)]
        self.fxcenter = self.fycenter = 0.5
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
    
    def step(self):
        for i in self.cornerx:
            if MC1.x+i > SCREEN_WIDTH1:
                MC1.x = SCREEN_WIDTH1-i
                Leftside.x = SCREEN_WIDTH1-i
            if MC1.x+i < 0:
                MC1.x = 0-i
                Leftside.x = SCREEN_WIDTH1-i
        for i in self.cornery:
            if MC1.y+i < 0:
                MC1.y = 0-i
                Leftside.y = 0-i
            if MC1.y+i > SCREEN_HEIGHT:
                MC1.y = SCREEN_HEIGHT-i
                Leftside.y = SCREEN_HEIGHT-i
        
        
        
            
    

class background(Sprite):
    def __init__(self, position):
        super().__init__(flashlight, position)
        self.fxcenter = self.fycenter = 0.5
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
        bg_asset = RectangleAsset(width, height, noline, white)
        bg = Sprite(bg_asset, (0,0))
    def step(self):
        
        MC1.step()
        
        
            


myapp = SpaceGame(SCREEN_WIDTH1, SCREEN_HEIGHT)
Leftside = background((320, 240))
MC1=MC((320,240))

myapp.run()