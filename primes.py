from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 570
class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        white = Color(0xffffff, 1)
# Background

        noline = LineStyle(0, black)
        
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, white)
        bg = Sprite(bg_asset, (0,0))
        
#Step Function
    def step(self):
        if generation == True:
            print("Yay")
            b = 0
            for x in primelist:
                print(x)
                if int(a)%int(x) != 0:
                    b += 1
                    print(b)
            if b == 0:
                primelist.append(a)
                a += 1
            else:              
                a+=1
myapp=Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
generation = False
def gen():
    global generation
    generation = not generation
def spaceKey(event):
    gen()
    print(primelist)
    print(generation)
myapp.listenKeyEvent('keydown', 'space', spaceKey)
a = 2
primelist=[1]

    
    

myapp.run()