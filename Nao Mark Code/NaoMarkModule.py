#Module for Nao Mark Visual Functions

# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import math
import almath

#Returns a multiple dimension array of naomark data
def getMarkData (IP, portNumber):
    #Set up the memory proxy.
    memoryProxy = ALProxy("ALMemory", IP, portNumber)

    #Set up the landmark proxy.
    landmarkProxy = ALProxy("ALLandMarkDetection", IP, portNumber)

    #Subscribe to landmarkDetected
    landmarkProxy.subscribe("GetLandMarkData")

    #Wait for a mark to be detected
    markData = memoryProxy.getData("LandmarkDetected")
    markData = memoryProxy.getData("LandmarkDetected")

    #Unsubscribe to proxy
    landmarkProxy.unsubscribe("GetLandMarkData")

    return markData

#Finds and returns a NaoMark's number
def getMarkNumber (markData):

    markNumber = markData[1][0][1][0]
    return markNumber

#Finds and returns the vertical and horiztontal
#offset of a nao mark relative to nao's camera
def getMarkAngles (markData):

    #Get the landmark positions(Relative to Camera)
    wzCamera = markData[1][0][0][1]
    wyCamera = markData[1][0][0][2]

    return wzCamera, wyCamera

#Finds and returns the x,y,z position of a nao mark
#relative to nao's camera
def getMarkXYZ (IP, portNumber, markData, landmarkSize):
    print "0"
    currentCamera = "CameraTop"
    print "1"
    # Retrieve landmark angular size in radians.
    angularSize = markData[1][0][0][3]
    print "2"
    # Compute distance to landmark.
    distanceFromCameraToLandmark = landmarkSize / ( 2 * math.tan( angularSize / 2))
    print "3"
    motionProxy = ALProxy("ALMotion", IP, portNumber)
    print "4"
    # Retrieve landmark center position in radians.
    wzCamera = markData[1][0][0][1]
    print "5"
    wyCamera = markData[1][0][0][2]
    print "6"
    # Get current camera position in NAO space.
    transform = motionProxy.getTransform(currentCamera, 2, True)
    print "7"
    transformList = almath.vectorFloat(transform)
    robotToCamera = almath.Transform(transformList)

    # Compute the rotation to point towards the landmark.
    cameraToLandmarkRotationTransform = almath.Transform_from3DRotation(0, wyCamera, wzCamera)

    # Compute the translation to reach the landmark.
    cameraToLandmarkTranslationTransform = almath.Transform(distanceFromCameraToLandmark, 0, 0)

    # Combine all transformations to get the landmark position in NAO space.
    robotToLandmark = robotToCamera * cameraToLandmarkRotationTransform *cameraToLandmarkTranslationTransform

    return robotToLandmark.r1_c4, robotToLandmark.r2_c4, robotToLandmark.r3_c4