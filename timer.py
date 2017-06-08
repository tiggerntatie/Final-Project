from ggame import Sprite, TextAsset
import time
time=60
def timer():
    time=time
    currentTime= time.time()
    timeList=[]
    def timer2():
        if time.time()-currentTime()>1:
            time-=1
            timeAsset=TextAsset(time)
            print(time, timeList)
            if len(timeList)>0:
                for x in timeList:
                    x.destroy
            timeList=[]
            timeList.append(Sprite(timeAsset, (200, 20)))
            print(timeList)
            timer()
        elif:
            timer2()
timer()
            
            
            
    
    
