from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset, CircleAsset
from math import pi, cos, sin, atan2, sqrt
import time
import random
#FIX spdSPRITE IDIOT
spriteCreate = 0
activated = []
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
        self.Created = 0
        self.production = 0
    def step(self):
        global activated
        if len(activated)>0:
            for x in activated:
                x.attack()
        
        for x in self.getSpritesbyClass(powerUp):
            x.step()
        for x in self.getSpritesbyClass(axe):
            x.step()
        for x in self.getSpritesbyClass(shield):
            x.step()
        for ship in self.getSpritesbyClass(bullet):
            ship.step()
        for ship in self.getSpritesbyClass(ShieldSprite):
            ship.step()
        for ship in self.getSpritesbyClass(spdSprite):
            if ship not in activated:
                ship.step()
        
                        
        global swordlist, bulletlist, maintain, movelist
        if turn == 1:
            x = 15+38*MC1.moves
            y=15
            lp = MC1.moves
            if MC1.moves==4:
                GG=1
            else:
                GG=0
            while GG != 1:
                movelist[lp]=Sprite(MCmoves,(myapp.width-15-x,y))
                if lp == speed1-1:
                    GG = 1
                    lp = 0
                else:
                    x+=38
                    lp+=1
            self.iterations +=1
            
            
            maintain = False
            for ship in self.getSpritesbyClass(sword):
                ship.destroy()
            
            for x in self.getSpritesbyClass(shield):
                x.destroy()
            if len(self.allSprites)>0:
                for x in self.allSprites:
                    x.step()
            MC1.step()
            MC1.shielded = -1
                
            global turn
            turn = 0
        if t == 0:
            MC1.hit2()
        if maintain == True:
            for ship in self.getSpritesbyClass(shootSprite):
                if ship.ndRd == 1:
                    ship.reload1()
        if spriteCreate == 1:
            print(self.numberofSprites)
            global spriteCreate
            spriteCreate = 0
            
            for _ in range(self.production//5+1):
                    self.create()
        for x in self.getSpritesbyClass(plasmaBolt):
            x.step()
    def create(self):
        self.Created +=1
        self.production +=1
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
        whatSprite= random.randint(1,5)
        print("newsprite",whatSprite, quad, xcolumn, self.width/2, ycolumn, self.height/2)
        self.allSprites.append(powerUp((xcolumn, ycolumn), random.randint(1,3), self.numberofSprites))
        """
        if whatSprite== 1:
            self.allSprites.append(meleeSprite((xcolumn,ycolumn), self.numberofSprites))
        elif whatSprite == 2:
            self.allSprites.append(shootSprite((xcolumn, ycolumn), random.randint(1,8), self.numberofSprites))
        elif whatSprite == 3:
            self.allSprites.append(ShieldSprite((xcolumn,ycolumn),random.randint(2,3), self.numberofSprites))
        elif whatSprite == 4:
            self.allSprites.append(spdSprite((xcolumn,ycolumn),random.randint(2,5), pi/2-atan2((ycolumn-240), (xcolumn-320)),self.numberofSprites))
            if whatSprite == 5:
                self.allSprites.append(powerUp((xcolumn, ycolumn), random.randint(1,3), self.numberofSprites))
        self.numberofSprites+=1
        """
myapp = SpaceGame(0,0)
bulletCount = 4
hit = 0
t=1
maintain = False
lives = 4
heartlist = list(range(4))
ammolist = list(range(bulletCount))

black = Color(0, 1)
speed = 10
speed1=4
movelist = list(range(speed1))
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
yellow = Color(0xffff00, 1.0)
yellow1 = Color(0xffff99, 1.0)
yellow2 = Color(0xe5e500, 1.0)
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
speedSprite = PolygonAsset(((-7.5,-11.5),(7.5,-11.5),(7.5,11.5),(-7.5,11.5)), thinline, black)
ss = PolygonAsset(((-7.5,-11.5),(7.5,-11.5),(7.5,11.5),(-7.5,11.5)), thinline, blue)
ShieldS = PolygonAsset(((-7.5,-11.5),(7.5,-11.5),(7.5,11.5),(-7.5,11.5)), thinline, green)
smlSword = PolygonAsset(((-2.5,-5),(2.5,-5),(2.5,5),(-2.5,5)), thinline, red)
smlBullet = PolygonAsset(((-2.5,0),(2.5,0),(2.5,-300),(-2.5,-300)), thinline, blue)
powerUpL = CircleAsset(10, noline, yellow)
powerUp1 = CircleAsset(10, noline, yellow1)
powerUp2 = CircleAsset(10, noline, yellow2)
MCshield = CircleAsset(25, noline,green)
MCmoves = CircleAsset(10, noline, black)
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
        SpaceGame.listenKeyEvent("keydown", "l", self.lKey)
        SpaceGame.listenKeyEvent("keydown", "r", self.rKey)
        self.fxcenter = self.fycenter = 0.5
        self.lives = ls
        self.start=0
        self.end=0
        self.dead = 0
        self.go = 0
        self.Sprites = []
        self.shielded = -1
        self.cooldownS = 0
        self.ammo = bulletCount
    def lKey(self, event):
        self.KILL()
        if self.moves >1 and self.cooldownS <1:
            shield((self.x,self.y))
            self.shielded = 2
            movelist[self.moves-1].destroy()
            self.moves -=1
            movelist[self.moves-1].destroy()
            self.moves -=1
            self.cooldownS=2
    def rKey(self,event):
        if self.moves >3:
            movelist[self.moves-1].destroy()
            self.moves -=1
            movelist[self.moves-1].destroy()
            self.moves -=1
            movelist[self.moves-1].destroy()
            self.moves -=1
            self.ammo = 4
            RELOAD()
    def jKey(self, event):
        self.KILL()
        if self.moves >0:
            self.Sprites.append(axe((self.x-60*cos((pi/2)-self.rotation), self.y -60*sin((pi/2)-self.rotation)), self.rotation))
            movelist[self.moves-1].destroy()
            self.moves -=1
    def kKey(self, event):
        self.KILL()
        if self.moves >2 and self.ammo>0:
            plasmaBolt((self.x-19*cos((pi/2)-self.rotation), self.y -19*sin((pi/2)-self.rotation)), self.rotation)
            movelist[self.moves-1].destroy()
            self.moves -=1
            movelist[self.moves-1].destroy()
            self.moves -=1
            movelist[self.moves-1].destroy()
            self.moves -=1
            ammolist[self.ammo-1].destroy()
            self.ammo -=1
    def dKey(self, event):
        self.KILL()
        if self.moves > 0 and self.x +speed*cos(self.rotation)<SCREEN_WIDTH1 and self.y -speed*sin(self.rotation) >0:
            self.x += speed*cos(self.rotation)
            self.y -= speed*sin(self.rotation)
            movelist[self.moves-1].destroy()
            self.moves -=1
    def aKey(self, event):
        self.KILL()
        if self.moves > 0 and self.x -speed*cos(self.rotation)>0 and self.y +speed*sin(self.rotation) <SCREEN_HEIGHT:
            self.x -= speed*cos(self.rotation)
            self.y += speed*sin(self.rotation)
            movelist[self.moves-1].destroy()

            self.moves -=1
    def sKey(self, event):
        self.KILL()
        if self.moves > 0 and self.x +speed*cos((pi/2)-self.rotation)<SCREEN_WIDTH1 and self.y +speed*sin((pi/2)-self.rotation) <SCREEN_HEIGHT:
            self.x += speed*cos((pi/2)-self.rotation)
            self.y += speed*sin((pi/2)-self.rotation)
            movelist[self.moves-1].destroy()
            self.moves -=1
    def wKey(self, event):
        self.KILL()
        if self.moves > 0 and self.x -speed*cos((pi/2)-self.rotation)>0 and self.y -speed*sin((pi/2)-self.rotation) >0:
           self.x -= speed*cos((pi/2)-self.rotation)
           self.y -= speed*sin((pi/2)-self.rotation)
           movelist[self.moves-1].destroy()
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
        if self.cooldownS>0:
            self.cooldownS-=1
    def hit(self):
        global t
        print('I got hit', self.shielded, t)
        if self.shielded >0:
            self.shielded -=1
        else:
            print("here")
            self.cooldownS = 0
            self.start = time.time()
            global heartlist
            self.lives -=1
            print(heartlist[self.lives])
            heartlist[self.lives].destroy()
            heartlist.remove(heartlist[self.lives])
            if t!=0:
                print('here 2')
                self.dead = Sprite(dead_asset, (1,1))
                print(self.dead)
                t=0
                self.end = self.start + .5
        
    def hit2(self):
        elapsed = time.time()
        if elapsed > self.end:
            print(self.dead)
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
    
        
class shield(Sprite):
    def __init__(self, position):
        super().__init__(MCshield, position)
    def step(self):
        self.x = MC1.x
        self.y= MC1.y
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
                
                if x.__class__.__name__ !='Sprite' and x.__class__.__name__ !='MC' and x.__class__.__name__ !='shield' and x.__class__.__name__ !='heart':
                    if x.__class__.__name__ =='ShieldSprite':
                        x.hp -=1
                    else:
                        if x in activated:
                            del activated[activated.index(x)]
                        print("hit", x.lp, len(myapp.allSprites))
                        del myapp.allSprites[myapp.allSprites.index(x)]
                        print(myapp.allSprites)
                        x.destroy()
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
                if x.__class__.__name__ !='Sprite' and x.__class__.__name__ !='MC' and x.__class__.__name__ !='shield' and x.__class__.__name__ !='heart':
                    if  x.__class__.__name__ =='shieldSprite':
                        x.hp -=1
                        self.destroy()
                    if x in activated:
                            del activated[activated.index(x)]
                    
                    print("hit", x.lp, x.__class__.__name__, myapp.allSprites[myapp.allSprites.index(x)],myapp.numberofSprites)
                    del myapp.allSprites[myapp.allSprites.index(x)]
                    print(myapp.allSprites,len(myapp.allSprites))
                    x.destroy()
                    print(myapp.numberofSprites)
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
class spdSprite(Sprite):
    def __init__(self, position, jumpTime,rotation,listposition): 
        super().__init__(speedSprite, position)
        self.fxcenter = self.fycenter = 0.5
        self.lp=listposition
        self.charge = 0
        self.jumpTime = jumpTime
        self.running = 0
        self.start = time.time()
        self.rotation = rotation
        self.q=rotation
    def step(self):
        global activated
        if self.running != 1:
            if time.time()-self.start>self.jumpTime:
                
                self.start = time.time()
                activated.append(myapp.allSprites[myapp.allSprites.index(self)])
                print(activated)
                
                self.running = 1
                
            else:
                self.rotation +=pi/60
    def attack(self):
        global activated
        if time.time()-self.start<self.jumpTime:
            self.x -= self.jumpTime*cos(-self.q+pi/2)
            self.y -= self.jumpTime*sin(-self.q+pi/2)
            if len(self.collidingWithSprites(MC))>0:
                del activated[ activated.index(self)]
                del myapp.allSprites[myapp.allSprites.index(self)]
                myapp.numberofSprites -=1
                MC1.hit()
                
                
                self.destroy()
        else:
            
            self.rotation = pi/2-atan2((self.y-MC1.y), (self.x-MC1.x))
            self.q = pi/2-atan2((self.y-MC1.y), (self.x-MC1.x))
            print(activated, activated.index(self))
            del activated[ activated.index(self)]
            print(activated)
            self.running = 0
            self.start = time.time()
                
        
class shootSprite(Sprite):
    def __init__(self, position, ammo, listposition): 
        super().__init__(ss, position)
        self.fxcenter = self.fycenter = 0.5
        self.ammo = ammo
        self.ammoMax = ammo
        self.lp=listposition
        self.ndRd = 0
    def step(self):
        if self.ndRd == 1:
            self.ndRd = 0
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
                self.ndRd =1
                self.ammo = self.ammoMax
                
    def reload1(self):
        self.rotation += pi/36
    
class bullet(Sprite):
    def __init__(self, position, rotation): 
        super().__init__(smlBullet, position)
        self.fxcenter = self.fycenter = 0.5
        self.rotation = rotation
        self.alive = time.time()
    def step(self):
        if time.time()-self.alive >.5:
            self.destroy()
        
        
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
        
        
    
class ammo(Sprite):
    asset = ImageAsset("imageedit_2_9797942232.png")
    def __init__(self, position, bulletnumber): 
        super().__init__(ammo.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.scale = .4
        self.bulletnumber=bulletnumber
class ShieldSprite(Sprite):
    def __init__(self, position, hp, listposition): 
        super().__init__(ShieldS, position)
        self.hp = hp
        self.fxcenter =  self.hp*4
        self.fycenter = 1
    def step(self):
        atan2(self.y-MC1.y, self.x-MC1.x)
        q = -1*pi/2+atan2(self.y-MC1.y, self.x-MC1.x)
        self.x += 2*cos(q)
        self.y+= 2*sin(q)
        self.rotation =  2*pi/2-atan2(self.y-MC1.y, self.x-MC1.x)
        if self.hp <1:
            self.destroy
class powerUp(Sprite):
    def __init__(self, position, assetNumber,listposition):
        print(assetNumber)
        if assetNumber == 1:
            self.asset = powerUpL
        elif assetNumber == 2:
            self.asset = powerUp1
        elif assetNumber == 3:
            self.asset = powerUp2
        super().__init__(self.asset, position)
        self.assetNumber = assetNumber
    def step(self):
        print("a")
        if len(self.collidingWithSprites(MC))>0:
            print("collected", self.assetNumber,self.assetNumber == 1,self.assetNumber == 2, myapp.allSprites[myapp.allSprites.index(self)])
            if self.assetNumber == 1:
                print("healed")
                heartlist.append(heart((heartlist[MC1.lives-1].x+38, 15), MC1.lives))
                print(heartlist)
                MC1.lives+=1
            elif self.assetNumber == 2:
                print('reload')
                MC1.rKey(0)
                print('reload')
            del myapp.allSprites[myapp.allSprites.index(self)]
            self.destroy()
            
            """
            elif self.powerUp == 3:
                for x in myapp.allSprites:
                    x.destroy()
                    myapp.allSprites=[]
                    myapp.numberofSprites = 0
            """
            
                
        



x = 15
y=15
lp = 0
GG = 0
while GG != 1:
    heartlist[lp]=heart((x,y), lp)
    movelist[lp]=Sprite(MCmoves,(myapp.width-15-x,y))
    if lp == lives-1:
        GG = 1
        lp = 0
    else:
        x+=38
        lp+=1

def RELOAD ():
    
    x = 15
    y=15
    lp = 0
    GG = 1
    
    
    while GG != 0:
        ammolist[lp]=ammo((myapp.width-15-x,myapp.height-y*3), lp)
        if lp == bulletCount-1:
            GG = 0
            lp = 0
        else:
            x+=38
            lp+=1
RELOAD()    
    
    
    
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
MC1=MC((myapp.width/2,myapp.height/2), lives)
myapp.run()