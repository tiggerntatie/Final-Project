from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 570
myapp=App()
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
b = 0
primelist=[1]
if generation == True:
    print("Yay")
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
    
    

myapp.run()