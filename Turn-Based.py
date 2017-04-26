from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from math import pi, cos, sin, atan2, sqrt
import time
SCREEN_WIDTH1 = 1024
hit = 0
t=1
maintain = False
lives = 4
heartlist = list(range(4))
SCREEN_HEIGHT = 571
black = Color(0, 1)
speed = 10
speed1=4
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
swordlist = []
bulletlist =[]
thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
noline = LineStyle(0, black)
thinline1 = LineStyle(1, white)
dead_asset = RectangleAsset(SCREEN_WIDTH1, SCREEN_HEIGHT, noline, red)
cf = PolygonAsset(((-10,-15),(0,-22.5),(10,-15),(10,15),(-10,15)), thinline, gray)
gameover = ImageAsset("game_over___pixel_art_by_tfcb93-d513cay.png")
ms = PolygonAsset(((-7.5,-11.5),(7.5,-11.5),(7.5,11.5),(-7.5,11.5)), thinline, red)
ss = PolygonAsset(((-7.5,-11.5),(7.5,-11.5),(7.5,11.5),(-7.5,11.5)), thinline, blue)
smlSword = PolygonAsset(((-2.5,-5),(2.5,-5),(2.5,5),(-2.5,5)), thinline, red)
smlBullet = PolygonAsset(((-2.5,-5),(2.5,-5),(2.5,5),(-2.5,5)), thinline, blue)
class MC(Sprite):
    def __init__(self, position, ls):
        super().__init__(cf, position)
        self.moves = speed1
        SpaceGame.listenKeyEvent("keydown", "d", self.dKey)
        SpaceGame.listenKeyEvent("keydown", "a", self.aKey)
        SpaceGame.listenKeyEvent("keydown", "s", self.sKey)
        SpaceGame.listenKeyEvent("keydown", "w", self.wKey)
        SpaceGame.listenKeyEvent("keydown", "q", self.qKey)
        SpaceGame.listenKeyEvent("keydown", "e", self.eKey)
        self.fxcenter = self.fycenter = 0.5
        self.lives = ls
        self.start=0
        self.end=0
        self.dead = 0
        self.go = 0
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
    def hit(self):
        self.start = time.time()
        global heartlist
        self.lives -=1
        heartlist[self.lives].destroy()
        heartlist.remove(heartlist[self.lives])
        self.dead = Sprite(dead_asset, (1,1))
        global t
        t=0
        self.end = self.start + .5
        
    def hit2(self):
        elapsed = time.time()
        if elapsed > self.end:
            print(self.lives)
            self.dead.destroy()
            global t
            t =1
            if self.lives == 0:
                self.go=Sprite(gameover, (1,1))
        
        
        
class meleeSprite(Sprite):
    def __init__(self, position): 
        super().__init__(ms, position)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.rotation = pi/2-atan2((self.y-MC1.y), (self.x-MC1.x))
        self.x -= 10*cos(atan2(self.y-MC1.y, self.x-MC1.x))
        self.y -= 10*sin(atan2(self.y-MC1.y, self.x-MC1.x))
        if MC1.rotation == 0 or MC1.rotation == pi:
            if sqrt((self.x-MC1.x)**2+(self.y-MC1.y)**2) <= 30:
                swordlist.append(sword(((self.x-15*cos(atan2(self.y-MC1.y, self.x-MC1.x))), (self.y-15*sin(atan2(self.y-MC1.y, self.x-MC1.x)))), self.rotation))
                MC1.hit()
        if MC1.rotation == pi/2 or MC1.rotation == 3*pi/2:
            if sqrt((self.x-MC1.x)**2+(self.y-MC1.y)**2) <= 30:
                swordlist.append(sword(((self.x-15*cos(atan2(self.y-MC1.y, self.x-MC1.x))), (self.y-15*sin(atan2(self.y-MC1.y, self.x-MC1.x)))), self.rotation))
                MC1.hit()
class shootSprite(Sprite):
    def __init__(self, position, ammo): 
        super().__init__(ss, position)
        self.fxcenter = self.fycenter = 0.5
        self.ammo = ammo
        self.ammoMax = ammo
    def step(self):
        self.rotation = pi/2-atan2((self.y-MC1.y), (self.x-MC1.x))
        if sqrt((self.x-MC1.x)**2+(self.y-MC1.y)**2) <= 150:
            self.x -= 10*cos(atan2(self.y-MC1.y, self.x-MC1.x))
            self.y -= 10*sin(atan2(self.y-MC1.y, self.x-MC1.x))
        else:
            if self.ammo>0:
                self.ammo-=1
                bulletlist.append(bullet(((self.x-20*cos(atan2(self.y-MC1.y, self.x-MC1.x))), (self.y-20*sin(atan2(self.y-MC1.y, self.x-MC1.x)))), self.rotation))
            else:
                global maintain
                maintain = True
                self.ammo = self.ammoMax
                print(self.ammo)
    def reload1(self):
        self.rotation += pi/36
    
class bullet(Sprite):
    def __init__(self, position, rotation): 
        super().__init__(smlBullet, position)
        self.fxcenter = self.fycenter = 0.5
        self.rotation = rotation
        self.time = time.time()
    def step(self):
        self.x -= 1*cos(-1*self.rotation+(pi/2))
        self.y -= 1*sin(-1*self.rotation+(pi/2))
        if self.collidingWithSprites(MC)>0:
            MC1.hit()
            self.destroy()
        elif time.time()-self.time > 5:
            self.destroy()
class sword(Sprite):
    def __init__(self, position, rotation): 
        super().__init__(smlSword, position)
        self.fxcenter = self.fycenter = 0.5
        self.rotation = rotation
    def step(self):
        self.x = self.y = 10000
class heart(Sprite):
    asset = ImageAsset("heart-e1403272720870.png")
    def __init__(self, position, heartnumber): 
        super().__init__(heart.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.scale = .05
        
        
    
    
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, .2)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        
        bg = Sprite(bg_asset, (0,0))
        
    def step(self):
        for x in self.getSpritesbyClass(meleeSprite):
            if len(x.collidingWithSprites(bullet))>0:
                    x.destroy()
        global swordlist, bulletlist, maintain
        
        if turn == 1:
            maintain = False
            for ship in self.getSpritesbyClass(sword):
                ship.destroy()
            
            
            
            swordlist=[]
            meleeSprite1.step()
            shootSprite1.step()
            MC1.step()
            
            global turn
            turn = 0
        if t == 0:
            MC1.hit2()
        if len(bulletlist)>0:
                for x in bulletlist:
                    x.step()
        if maintain == True:
            for ship in self.getSpritesbyClass(shootSprite):
                ship.reload1()
            
            
            
   


myapp = SpaceGame(SCREEN_WIDTH1,SCREEN_HEIGHT)

x = 15
y=15
lp = 0
GG = 0
while GG != 1:
    heartlist[lp]=heart((x,y), lp)
    if lp == lives-1:
        GG = 1
    else:
        x+=38
        lp+=1
    
    
turn = 0
def turnProgress ():
    if MC1.lives>0:
        global turn
        turn=1
def spaceKey (event):
    
    turnProgress()
    
    
    
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)
MC1=MC((320,240), lives)
meleeSprite1=meleeSprite((300,240))
shootSprite1=shootSprite((100,100), 4)
myapp.run()