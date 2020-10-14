# import Python modules
import os
import datetime
import time

# define directory to work with
myFolder = "myFolder/"

# initialize current time
timeNow = datetime.datetime.now()

# time delta to check files
# measured in seconds
timeDelta = 60

def readTimeFile(pathFile):
  modificationTime = os.path.getmtime(pathFile)
  return modificationTime

def readTimeFolder(directoryFile):
  for fileName in os.listdir(directoryFile):
    fullPath = os.path.join(directoryFile, fileName)
    modificationTime = readTimeFile(fullPath)
    # print(time.ctime(modificationTime))
    modificationTime = datetime.datetime.fromtimestamp(modificationTime).strftime('%Y-%m-%d %H:%M:%S')
    return modificationTime

while True:
  timeNow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print("timeNow:")
  print(timeNow)
  timeFile = readTimeFolder(myFolder)
  print("timeFile: ")
  print(timeFile)
  time.sleep(timeDelta)
