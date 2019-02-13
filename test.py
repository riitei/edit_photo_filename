import datetime
import os, time




file = '20190204_IMG_4788.PNG'
path = 'C:\iPhone X/'+file



timeStamp = os.stat(path).st_mtime   #文件的修改时间
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y %m %d %H:%M:%S", timeArray)
print(otherStyleTime)


print(os.path.splitext(path)[-1])