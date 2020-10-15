# a project by nicole l'huillier + aarón montoya-moraga
# october 2020

# import Python modules
import os
import pathlib
import datetime
import time

# import Python modules
import  vlc

mediaPlayer = vlc.MediaPlayer() 

# folder to work with
myFolder = "myFolder/"

# time interval between repetitions, measured in seconds
timeInterval = 10
timeIntervalDate = datetime.timedelta(seconds=timeInterval)

# file extensions for audio
extensions = [".mp3", ".wav"]

# function for reading times of modification
def readModificationTimes(directoryFile):
  modificationTimes = []
  fileNames = []
  for fileName in os.listdir(directoryFile):

    # retrieve full path
    fullPath = os.path.join(directoryFile, fileName)

    # retrieve extension
    extension = pathlib.PurePath(fullPath).suffix

    # if extension is an audio extension
    if (extension in extensions):
      
      # retrieve its modification time
      modificationTime = os.path.getmtime(fullPath)
      # convert to date
      modificationTime = datetime.datetime.fromtimestamp(modificationTime)
      
      # append time to the array
      modificationTimes.append(modificationTime)
      # append filename to the array
      fileNames.append(fullPath)
  
  # return arrays
  return modificationTimes, fileNames

# check if files are expired
def checkExpiration(fileTimes, fileNames, timeNow):

  isExpired = []
  
  # go through every time
  for index in range(len(fileTimes)):
    # calculate time between timeNow and each fileTime
    difference = timeNow - fileTimes[index]

    # check if difference is bigger than the interval
    if (difference > timeIntervalDate):
      isExpired.append(True)
    else:
      isExpired.append(False)
  
  return isExpired
    
def playAndDelete(fileNames, isExpired):

  # go through every file
  for index in range(len(fileNames)):

    if (isExpired[index]):
      # play the file
      media = vlc.Media(fileNames[index])
      mediaPlayer.set_media(media)
      mediaPlayer.play()
      # getting length of the current media 
      mediaLength = mediaPlayer.get_length()
      time.sleep(mediaLength)
      # delete the file
      os.remove(fileNames[index])

# infinite loop
while True:

  # update current time
  timeNow = datetime.datetime.now()
  print(timeNow)
  
  # get array of times of modification of files
  fileTimes, fileNames = readModificationTimes(myFolder)

  # go through every file and decide
  isExpired = checkExpiration(fileTimes, fileNames, timeNow)

  playAndDelete(fileNames, isExpired)

  print("")

  # wait before next iteration
  time.sleep(timeInterval)
