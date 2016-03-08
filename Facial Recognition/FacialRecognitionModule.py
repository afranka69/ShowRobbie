#Module for Nao Mark Visual Functions

# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import math
import almath
import time

def getFaceData(IP, PORT):
    #make proxy to face detection
    faceProxy = ALProxy("ALFaceDetection", IP, PORT)

    #Make proxy to memory
    memoryProxy = ALProxy("ALMemory", IP, PORT)

    faceProxy.subscribe("GetFaceData")

    faceData = memoryProxy.getData("FaceDetected")
    faceProxy.unsubscribe("GetFaceData")

    return faceData

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

#return name of a face
def getFaceName (faceData):
    return faceData[1][0][1][2]

#Return the confidence of a face
def getFaceConfidince (faceData):
    return faceData[1][0][1][1]

