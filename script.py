# import os
import os
import datetime
import time

# define directory to work with
myDirectory = "myFiles/"

# initialize current time
timeNow = datetime.datetime.now()
print(timeNow)

# time delta to check files
deltaTime = 4

def readModificationTime(fullPath):
  modifcationTime = os.path.getmtime(fullPath)
  return modifcationTime

for filename in os.listdir(myDirectory):
  fullPath = os.path.join(myDirectory, filename)
  modificationTime = readModificationTime(fullPath)
  print(time.ctime(modificationTime))
  modificationTime = datetime.datetime.fromtimestamp(modificationTime).strftime('%Y-%m-%d %H:%M:%S')
  print(modificationTime)
