from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
SCREEN_WIDTH1 = 640
SCREEN_HEIGHT = 480
black = Color(0, 1)
speed = 4
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)


thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
noline = LineStyle(0, black)
thinline1 = LineStyle(1, white)
cf = PolygonAsset(((-10,-15),(10,-15),(10,15),(-10,15)), thinline, gray)
class MC(Sprite):
    def __init__(self, position):
        super().__init__(cf, position)
        self.moves = speed
        SpaceGame.listenKeyEvent("keydown", "d", self.dKey)
        SpaceGame.listenKeyEvent("keydown", "a", self.aKey)
        SpaceGame.listenKeyEvent("keydown", "s", self.sKey)
        SpaceGame.listenKeyEvent("keydown", "w", self.wKey)
        SpaceGame.listenKeyEvent("keydown", "e", self.eKey)
        SpaceGame.listenKeyEvent("keydown", "q", self.qKey)
    def dKey(self, event):
        if self.moves > 0:
            self.x += 10
            moves -=1
    def aKey(self, event):
        if self.moves > 0:
            self.x -= 10
            moves -=1
    def sKey(self, event):
        if self.moves > 0:
            self.y -= 10
            moves -=1
    def wKey(self, event):
        if self.moves > 0:
            self.y += 10
            moves -=1
    def step(self):
        if turn == 1:
            turn = 0
            self.moves = speed
        
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
        
       
            


myapp = SpaceGame(SCREEN_WIDTH1, SCREEN_HEIGHT)

turn = 0
def turnProgress (event):
    global turn = 1
def spaceKey (event):
    turnProgress()
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)



myapp.run()