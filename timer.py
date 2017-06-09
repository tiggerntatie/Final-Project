from ggame import Sprite, TextAsset
import time
timeCounter=60
cT= time.time()
timeList=[]
timeReset = False
def timer():
    print('hi')
    global cT, timeCounter, timeList, timeReset
    if timeReset==True:
        print('hi')
        cT=time.time
        timeReset=False
    elif time.time()-cT>1:
        if len(timeList)>0:
            for x in timeList:
                x.destroy()
        timeAsset= TextAsset(timeCounter)
        timeList.append(Sprite(timeAsset, (100,100)))
        timeReset = True
        print(timeList)
timer()
        
            
    
    
