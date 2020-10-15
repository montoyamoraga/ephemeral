# a project by nicole l'huillier + aarón montoya-moraga
# october 2020

# import Python modules
import os
import datetime
import time

# import Python modules
import  vlc

# define folder to work with
myFolder = "myFolder/"

# time interval to check files, measured in seconds
timeInterval = 10
timeIntervalDate = datetime.timedelta(seconds=timeInterval)

def readTimeFolder(directoryFile):
  modificationTimes = []
  fileNames = []
  for fileName in os.listdir(directoryFile):
    fullPath = os.path.join(directoryFile, fileName)
    modificationTime = os.path.getmtime(fullPath)
    modificationTime = datetime.datetime.fromtimestamp(modificationTime)
    
    modificationTimes.append(modificationTime)
    fileNames.append(fullPath)
  
  # return array
  return modificationTimes, fileNames

def checkIfFilesExpire(modificationTimes, fileNames, timeNow):

  for index in range(len(modificationTimes)):
    difference = timeNow - modificationTimes[index]

    if (difference > timeIntervalDate):
      print("playing the file:" + fileNames[index])
      p = vlc.MediaPlayer(fileNames[index])

while True:
  # update current time
  timeNow = datetime.datetime.now()
  print(timeNow)

  # get array of times of modification of files
  fileTimes, fileNames = readTimeFolder(myFolder)

  # go through every file and decide
  checkIfFilesExpire(fileTimes, fileNames, timeNow)

  # wait before next iteration
  time.sleep(timeInterval)
