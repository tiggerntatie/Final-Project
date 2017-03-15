from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 570
myapp=App()
generation = False

primelist=[1]
def gen():
    a = len(primelist)+1
    b= 0
    i = 0
    while i !=1:
        print("Yay", a)
        for x in primelist:
            print("1st step")
            if int(a)%int(x) == 0:
                b += 1
        if b == 1:
            primelist.append(a)
            a += 1
            print("Success")
            print("Not a prime")
            i=1
        else:              
            a+=1
            
def spaceKey(event):
    gen()
    print(primelist)
myapp.listenKeyEvent('keydown', 'space', spaceKey)


    
    

myapp.run()