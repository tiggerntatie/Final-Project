from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from math import pi, cos, sin, atan2, sqrt
SCREEN_WIDTH1 = 640
SCREEN_HEIGHT = 480
black = Color(0, 1)
speed = 10
speed1=4
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
swordlist = []

thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
noline = LineStyle(0, black)
thinline1 = LineStyle(1, white)
cf = PolygonAsset(((-10,-15),(10,-15),(10,15),(-10,15)), thinline, gray)
ms = PolygonAsset(((-7.5,-11.5),(7.5,-11.5),(7.5,11.5),(-7.5,11.5)), thinline, red)
smlSword = PolygonAsset(((-2.5,-5),(2.5,-5),(2.5,5),(-2.5,5)), thinline, red)
class MC(Sprite):
    def __init__(self, position):
        super().__init__(cf, position)
        self.moves = speed1
        SpaceGame.listenKeyEvent("keydown", "d", self.dKey)
        SpaceGame.listenKeyEvent("keydown", "a", self.aKey)
        SpaceGame.listenKeyEvent("keydown", "s", self.sKey)
        SpaceGame.listenKeyEvent("keydown", "w", self.wKey)
        SpaceGame.listenKeyEvent("keydown", "q", self.qKey)
        SpaceGame.listenKeyEvent("keydown", "e", self.eKey)
        self.fxcenter = self.fycenter = 0.5
    def dKey(self, event):
        if self.moves > 0 and self.x +speed*cos(self.rotation)<SCREEN_WIDTH1 and self.y -speed*sin(self.rotation) >0:
            self.x += speed*cos(self.rotation)
            self.y -= speed*sin(self.rotation)
            self.moves -=1
    def aKey(self, event):
        if self.moves > 0 and self.x -speed*cos(self.rotation)>0 and self.y +speed*sin(self.rotation) <SCREEN_HEIGHT:
            self.x -= speed*cos(self.rotation)
            self.y += speed*sin(self.rotation)

            self.moves -=1
    def sKey(self, event):
        if self.moves > 0 and self.x +speed*cos((pi/2)-self.rotation)<SCREEN_WIDTH1 and self.y +speed*sin((pi/2)-self.rotation) <SCREEN_HEIGHT:
            self.x += speed*cos((pi/2)-self.rotation)
            self.y += speed*sin((pi/2)-self.rotation)
            self.moves -=1
    def wKey(self, event):
        if self.moves > 0 and self.x -speed*cos((pi/2)-self.rotation)>0 and self.y -speed*sin((pi/2)-self.rotation) >0:
           self.x -= speed*cos((pi/2)-self.rotation)
           self.y -= speed*sin((pi/2)-self.rotation)
           self.moves-=1
    def qKey(self, event):
        if self.rotation == 3*(pi/2):
            self.rotation = 0
        else:
            self.rotation+= pi/2
    def eKey(self, event):
        if self.rotation == -3*(pi/2):
            self.rotation = 0
        else:
            self.rotation-= pi/2
    def step(self):
        
        self.moves = speed1
class meleeSprite(Sprite):
    def __init__(self, position): 
        super().__init__(ms, position)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.rotation = pi/2-atan2((self.y-MC1.y), (self.x-MC1.x))
        self.x -= 10*cos(atan2(self.y-MC1.y, self.x-MC1.x))
        self.y -= 10*sin(atan2(self.y-MC1.y, self.x-MC1.x))
        
        if MC1.rotation == 0 or MC1.rotation == pi:
            if sqrt((self.x-MC1.x)**2+(self.y-MC1.y)**2) <= 20:
                print("yay")
                swordlist.append(sword(((self.x-15*cos(atan2(self.y-MC1.y, self.x-MC1.x))), (self.y-15*sin(atan2(self.y-MC1.y, self.x-MC1.x)))), self.rotation))
class sword(Sprite):
    def __init__(self, position, rotation): 
        super().__init__(smlSword, position)
        self.fxcenter = self.fycenter = 0.5
        self.rotation = rotation
        
    
    
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
        if turn == 1:
            for x in swordlist:
                x.destroy
            
            meleeSprite1.step()
            MC1.step()
            global turn
            turn = 0
        
            


myapp = SpaceGame(SCREEN_WIDTH1, SCREEN_HEIGHT)

turn = 0
def turnProgress ():
    global turn
    turn=1
def spaceKey (event):
    turnProgress()
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)
MC1=MC((320,240))
meleeSprite1=meleeSprite((300,240))

myapp.run()