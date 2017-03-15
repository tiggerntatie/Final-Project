from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
myapp=App()
generation = False
def gen():
    global generation
    generation = not generation
def spaceKey(event):
    gen()
    print(primelist)
myapp.listenKeyEvent('keydown', 'space', spaceKey)
a = 2
primelist=[1]
while generation == True:
    b = 0
    for x in primelist:
        if int(a)%int(x) != 0:
            b += 1
    if b == 1:
        primelist.append(a)
        a += 1
    else:
        a+=1
    
    
a = sum(primelist)
myapp.run()