from ggame import Sprite, TextAsset
import time
timeCounter=60
cT= time.time()
timeList=[]
def timer():
    global timeCounter, cT, timeList
    timeCounter=timeCounter
    cT= time.time()
    timeList=[]
    print(cT)
    def timer2():
        global timeCounter, cT, timeList
        if time.time()-cT>1:
            timeCounter-=1
            timeAsset=TextAsset(time)
            print(timeCounter, timeList) 
            
        else:
            
    timer2()
       
timer()
            
            
            
    
    
