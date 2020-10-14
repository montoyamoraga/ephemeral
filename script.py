# import Python modules
import os
import datetime
import time

# define folder to work with
myFolder = "myFolder/"

# time interval to check files, measured in seconds
timeInterval = 10
timeIntervalDate = datetime.timedelta(seconds=timeInterval)

def readTimeFile(pathFile):
  modificationTime = os.path.getmtime(pathFile)
  return modificationTime

def readTimeFolder(directoryFile):
  modificationTimes = []
  for fileName in os.listdir(directoryFile):
    fullPath = os.path.join(directoryFile, fileName)
    modificationTime = readTimeFile(fullPath)
    modificationTime = datetime.datetime.fromtimestamp(modificationTime)
    modificationTimes.append(modificationTime)
  
  # return array
  return modificationTimes

def checkIfFilesExpire(modificationTimes, timeNow):

  for index in range(len(modificationTimes)):
    difference = timeNow - modificationTimes[index]

    if (difference > timeIntervalDate):
      print("this file should be played and deleted")
    else:
      print("this file should wait")


while True:
  # update current time
  timeNow = datetime.datetime.now()
  print(timeNow)

  # get array of times of modification of files
  fileTimes = readTimeFolder(myFolder)

  # go through every file and decide
  checkIfFilesExpire(fileTimes, timeNow)

  # wait before next iteration
  time.sleep(timeInterval)
