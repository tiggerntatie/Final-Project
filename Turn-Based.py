from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from math import pi, cos, sin, atan2, sqrt
import time
import random
spriteCreate = 0
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, .2)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        
        self.bg = Sprite(bg_asset, (0,0))
        global SCREEN_WIDTH1, SCREEN_HEIGHT
        SCREEN_WIDTH1=self.width
        SCREEN_HEIGHT = self.height
        self.allSprites = []
        self.iterations = 0
        self.numberofSprites = 0
    def step(self):
        
        
        for x in self.getSpritesbyClass(plasmaBolt):
            x.step()
        for x in self.getSpritesbyClass(axe):
            x.step()
        
                        
        global swordlist, bulletlist, maintain
        if turn == 1:
            self.iterations +=1
            
            maintain = False
            for ship in self.getSpritesbyClass(sword):
                ship.destroy()
            for ship in self.getSpritesbyClass(bullet):
                ship.destroy()
            if len(self.allSprites)>0:
                for x in self.allSprites:
                    x.step()
            MC1.step()
                
            global turn
            turn = 0
        if t == 0:
            MC1.hit2()
        if maintain == True:
            for ship in self.getSpritesbyClass(shootSprite):
                ship.reload1()
        if spriteCreate == 1:
            global spriteCreate
            spriteCreate = 0
            if self.numberofSprites>5:
                for _ in range(3):
                    self.create()
            self.create()
    def create(self):
        quad = random.randint(1,4)
        if quad == 1:
            xcolumn = self.width/2+30*random.randint(1,(self.width/2)//30)
            ycolumn = 30*random.randint(1,(self.height/2)//30)
        elif quad == 2:
            xcolumn = 30*random.randint(1,(self.width/2)//30)
            ycolumn = 30*random.randint(1,(self.height/2)//30)
        elif quad == 3:
            xcolumn = 30*random.randint(1,(self.width/2)//30)
            ycolumn = self.height/2+random.randint(1,(self.height/2)//30)
        else:
            xcolumn = self.width/2+random.randint(1,(self.width/2)//30)
            ycolumn = self.height/2+random.randint(1,(self.height/2)//30)
        whatSprite= random.randint(1,2)
        print(whatSprite, quad, xcolumn, self.width/2, ycolumn, self.height/2)
        if whatSprite== 1:
            self.allSprites.append(meleeSprite((xcolumn,ycolumn), self.numberofSprites))
        elif whatSprite == 2:
            self.allSprites.append(shootSprite((xcolumn, ycolumn), random.randint(1,8), self.numberofSprites))
        self.numberofSprites+=1
myapp = SpaceGame(0,0)
hit = 0
t=1
maintain = False
lives = 4
heartlist = list(range(4))

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
smlBullet = PolygonAsset(((-2.5,0),(2.5,0),(2.5,-300),(-2.5,-300)), thinline, blue)
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
        SpaceGame.listenKeyEvent("keydown", "j", self.jKey)
        SpaceGame.listenKeyEvent("keydown", "k", self.kKey)
        self.fxcenter = self.fycenter = 0.5
        self.lives = ls
        self.start=0
        self.end=0
        self.dead = 0
        self.go = 0
        self.Sprites = []
    def jKey(self, event):
        self.KILL()
        if self.moves >0:
            self.Sprites.append(axe((self.x-60*cos((pi/2)-self.rotation), self.y -60*sin((pi/2)-self.rotation)), self.rotation))
            self.moves -=1
    def kKey(self, event):
        self.KILL()
        if self.moves >2:
            plasmaBolt((self.x-19*cos((pi/2)-self.rotation), self.y -19*sin((pi/2)-self.rotation)), self.rotation)
            self.moves -=3
    def dKey(self, event):
        self.KILL()
        if self.moves > 0 and self.x +speed*cos(self.rotation)<SCREEN_WIDTH1 and self.y -speed*sin(self.rotation) >0:
            self.x += speed*cos(self.rotation)
            self.y -= speed*sin(self.rotation)
            self.moves -=1
    def aKey(self, event):
        self.KILL()
        if self.moves > 0 and self.x -speed*cos(self.rotation)>0 and self.y +speed*sin(self.rotation) <SCREEN_HEIGHT:
            self.x -= speed*cos(self.rotation)
            self.y += speed*sin(self.rotation)

            self.moves -=1
    def sKey(self, event):
        self.KILL()
        if self.moves > 0 and self.x +speed*cos((pi/2)-self.rotation)<SCREEN_WIDTH1 and self.y +speed*sin((pi/2)-self.rotation) <SCREEN_HEIGHT:
            self.x += speed*cos((pi/2)-self.rotation)
            self.y += speed*sin((pi/2)-self.rotation)
            self.moves -=1
    def wKey(self, event):
        self.KILL()
        if self.moves > 0 and self.x -speed*cos((pi/2)-self.rotation)>0 and self.y -speed*sin((pi/2)-self.rotation) >0:
           self.x -= speed*cos((pi/2)-self.rotation)
           self.y -= speed*sin((pi/2)-self.rotation)
           self.moves-=1
    def qKey(self, event):
        self.KILL()
        if self.rotation == 31*(pi/32):
            self.rotation = 0
        else:
            self.rotation+= pi/32
    def eKey(self, event):
        self.KILL()
        if self.rotation == -31*(pi/32):
            self.rotation = 0
        else:
            self.rotation-= pi/32
    def KILL(self):
        if len(self.Sprites)>0:
            for x in self.Sprites:
                x.destroy()
                
            self.Sprites = []
    def step(self):
        self.KILL()
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
            self.dead.destroy()
            global t
            t =1
            if self.lives == 0:
                if SCREEN_WIDTH1/1071<SCREEN_HEIGHT/571:
                    self.go=Sprite(gameover, (1,1))
                    self.go.scale = SCREEN_WIDTH1/1071
                else:
                    self.go=Sprite(gameover, (1,1))
                    self.go.scale = SCREEN_HEIGHT/571
class axe(Sprite):
    
    def __init__(self, position, rotation): 
        asset = ImageAsset("download.png", Frame(56.25, 56.25, 56.25*2, 56.25*2.1))
        super().__init__(asset, position)
        self.scale = .3
        self.fxcenter = .5
        self.fycenter = 0
        self.rotation = rotation
    def step(self):
        if len(self.collidingWithSprites(None))>0:
            for x in self.collidingWithSprites(None):
                
                if x.__class__.__name__ !='Sprite' and x.__class__.__name__ !='MC':
                    x.destroy()
                    print("hit", x.lp)
                    del myapp.allSprites[x.lp]
                    for i in myapp.allSprites:
                        if i.lp>x.lp:
                            i.lp-=1
                    myapp.numberofSprites -=1
        
class plasmaBolt(Sprite):
    
    def __init__(self, position, rotation): 
        asset = ImageAsset("plasma-weapon-fire-animation.png")
        
        super().__init__(asset, position)
        self.scale = .1
        self.fxcenter = .5
        self.fycenter = 1
        self.rotation = rotation
        self.time = time.time()
    def step(self):
        self.x -=1.5*cos((pi/2)-self.rotation)
        self.y -=1.5*sin((pi/2)-self.rotation)
        if len(self.collidingWithSprites(None))>0:
            for x in self.collidingWithSprites(None):
                if x.__class__.__name__ !='Sprite' and x.__class__.__name__ !='MC':
                    x.destroy()
                    print("hit", x.lp)
                    del myapp.allSprites[x.lp]
                    for i in myapp.allSprites:
                        if i.lp>x.lp:
                            i.lp-=1
                    myapp.numberofSprites -=1
                    
        if -self.time+time.time()>10:
            self.destroy()
        
        
class meleeSprite(Sprite):
    def __init__(self, position, listposition): 
        super().__init__(ms, position)
        self.fxcenter = self.fycenter = 0.5
        self.lp=listposition
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
    def __init__(self, position, ammo, listposition): 
        super().__init__(ss, position)
        self.fxcenter = self.fycenter = 0.5
        self.ammo = ammo
        self.ammoMax = ammo
        self.lp=listposition
    def step(self):
        self.rotation = pi/2-atan2((self.y-MC1.y), (self.x-MC1.x))
        if sqrt((self.x-MC1.x)**2+(self.y-MC1.y)**2)-300>1:
            self.x -= 10*cos(atan2(self.y-MC1.y, self.x-MC1.x))
            self.y -= 10*sin(atan2(self.y-MC1.y, self.x-MC1.x))
        else:
            if self.ammo>0:
                self.ammo-=1
                MC1.hit()
                bulletlist.append(bullet(((self.x-15*cos(atan2(self.y-MC1.y, self.x-MC1.x))), (self.y-15*sin(atan2(self.y-MC1.y, self.x-MC1.x)))), self.rotation))
            else:
                global maintain
                maintain = True
                self.ammo = self.ammoMax
                
    def reload1(self):
        self.rotation += pi/36
    
class bullet(Sprite):
    def __init__(self, position, rotation): 
        super().__init__(smlBullet, position)
        self.fxcenter = self.fycenter = 0.5
        self.rotation = rotation
        
        
class sword(Sprite):
    def __init__(self, position, rotation): 
        super().__init__(smlSword, position)
        self.fxcenter = self.fycenter = 0.5
        self.rotation = rotation
class heart(Sprite):
    asset = ImageAsset("heart-e1403272720870.png")
    def __init__(self, position, heartnumber): 
        super().__init__(heart.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.scale = .05
        
        
    
    

   




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
        if myapp.iterations>4:
            myapp.iterations = 0
            global spriteCreate
            spriteCreate = 1
def spaceKey (event):
    turnProgress()
myapp.create()
    
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)
MC1=MC((320,240), lives)
myapp.run()