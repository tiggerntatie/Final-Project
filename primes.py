from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
generation = False
def gen():
    global generation
    generation = not generation
def spaceKey(event):
    gen()
myapp.listenKeyEvent('keydown', 'space', spaceKey)
a = 1
primelist=[1]
while generation == True:
    b = 0
    for x in primelist:
        if a//x = 0:
            b += 1
    if b == 0:
        primelist.append(a)
        a += 1
    else:
        a+=1
    
    
a = sum(primelist)
myapp.run()