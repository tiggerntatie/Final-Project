from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 570
myapp=App()
generation = False
a = 2
b = 0
primelist=[1]
def gen():
    print("Yay")
    for x in primelist:
        print(x, "1st step")
        if int(a)%int(x) != 0:
            b += 1
            print(b)
    if b == 0:
        primelist.append(a)
        a += 1
        print("Success")
    else:              
        a+=1
def spaceKey(event):
    gen()
    print(primelist)
    print(generation)
myapp.listenKeyEvent('keydown', 'space', spaceKey)


    
    

myapp.run()