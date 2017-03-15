from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 570
myapp=App()
generation = False

primelist=[1]

a = 2
b= 0

   
def spaceKey(event):
    i = 0
    global a
    global b
    while i !=10:
        print("Yay", a)
        for x in primelist:
            print("1st step")
            if int(a)%int(x) == 0:
                b += 1
        if b == 1:
            primelist.append(a)
            a += 1
            print("Success")
            i+=1
        else:              
            a+=1
            print("Not a prime")
            i+=1
    print(primelist)
myapp.listenKeyEvent('keydown', 'space', spaceKey)


    
    

myapp.run()