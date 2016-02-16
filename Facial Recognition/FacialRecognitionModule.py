#Module for Nao Mark Visual Functions

# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import math
import almath
import time

#Tells nao to learn a associate face
#with passed name
def learnFace (IP, PORT, Name):
    #make proxy to face detection
    faceProxy = ALProxy("ALFaceDetection", IP, PORT)
    return faceProxy.learnFace(Name)

#Tells nao to remove all remembered faces
def clearFaceDatabase (IP, PORT):
    #make proxy to face detection
    faceProxy = ALProxy("ALFaceDetection", IP, PORT)
    faceProxy.clearDatabase()

#identifies and returns the name and confidence level
#of a recognized face or null if a face is not found.
def getFaceName (IP, PORT):
    #make proxy to face detection
    faceProxy = ALProxy("ALFaceDetection", IP, PORT)

    #Make proxy to memory
    memoryProxy = ALProxy("ALMemory", IP, PORT)

    #Make proxy to speech
    speechProxy = ALProxy("ALTextToSpeech", IP, PORT)

    faceProxy.subscribe("GetFaceData")

    faceData = memoryProxy.getData("FaceDetected")
    faceProxy.unsubscribe("GetFaceData")

    #Face not found, send data to signal this
    if (faceData is None or len(faceData) == 0):
        return 0, "null"
    #face found return data
    else:
        faceInfo = faceData[1][0][1]
        conf = faceInfo[1]
        name = faceInfo[2]
        return conf, name

