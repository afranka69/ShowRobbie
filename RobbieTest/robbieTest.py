import argparse
import motion
import time
import almath
import NaoMarkModule
import BotFreezerModule
import BrokerController
import NonBlockWalk

from naoqi import ALProxy
robotIP = "10.0.0.7"
PORT = 9559
postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
naomarkSize = .148;

lifeProxy = ALProxy("ALAutonomousLife", robotIP, PORT)
tts = ALProxy("ALTextToSpeech", robotIP, PORT)
motionProxy = ALProxy("ALMotion", robotIP, PORT)
curAngle = 0


def turnRight90():
    motionProxy.moveInit()
    time.sleep(1)
    global curAngle
    motionProxy.moveTo(0, 0, curAngle -1.57)
    curAngle += -1.57

def lookAround():
    motionProxy.moveInit()
    time.sleep(1)

    names = "HeadYaw"
    angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
    times      = [1.0,  2.0, 3.0,  4.0, 5.0]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

def lookTo(angle):
    motionProxy.moveInit()
    time.sleep(1)

    motionProxy.changeAngles("HeadYaw", angle,.1)

def lookAroundForMark():
    motionProxy.moveInit()
    time.sleep(1)

    names = "HeadYaw"
    markFound = False
    angleLists = .25
    back = False
    markData = NaoMarkModule.getMarkData(robotIP, PORT)
    first = True

    while(not markFound):

        if (back):
            angleLists = angleLists -.125
        else: angleLists = angleLists + .125

        if(angleLists > 1.0):
            angleLists = 1.0
            back = True
        else:
            if(angleLists < -1.0):
                angleLists = -1.0
                back = False


        times = .15
        if(first):
            times = 1.0
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

        markData = NaoMarkModule.getMarkData(robotIP, PORT)

        if(not (markData is None or len(markData) ==0)):
            markFound =True
        first = False
    return markData

def turnToHeadStraight(markData):
     motionProxy.moveInit()
     time.sleep(1)
     global curAngle

     deltaAngle,dontcare = NaoMarkModule.getMarkAngles(markData)

     angle = motionProxy.getAngles("HeadYaw",False)
     print angle[0]

     motionProxy.moveTo(0, 0, angle[0])
     print "Moved to head straight"


def detectMarkWalkStraight():
    markD =  lookAroundForMark()
    global naomarkSize
    x,y,z = NaoMarkModule.getMarkXYZ(robotIP, PORT, markD, naomarkSize)
    turnToHeadStraight(markD)
    detectMarkAndMoveTo()


def turnLeft90():
    motionProxy.moveInit()
    time.sleep(1)
    global curAngle
    motionProxy.moveTo(0, 0, curAngle + 1.57)
    curAngle += 1.57

def turnAround():
    motionProxy.moveInit()
    time.sleep(1)
    global curAngle
    motionProxy.moveTo(0,0, curAngle - 3.14)
    curAngle += -3.14

def moveForward(distance):
    motionProxy.moveInit()
    time.sleep(1)
    motionProxy.moveTo(distance, 0, 0)

def moveForwardY(distance, y):
    motionProxy.moveInit()
    time.sleep(1)
    motionProxy.moveTo(distance, y, 0)

def moveStrafe(distance, theta):
    motionProxy.moveInit()
    time.sleep(1)
    motionProxy.moveTo(distance, 0, theta)

def wave():
    time.sleep(1)
    names = ["RShoulderRoll", "RShoulderPitch", "RElbowYaw","RWristYaw", "RElbowRoll"]

    motionProxy.openHand("RHand")
    angleLists = [[-75.0*almath.TO_RAD], [0.0*almath.TO_RAD], [60.0*almath.TO_RAD],[60*almath.TO_RAD],[0.0*almath.TO_RAD,87.0*almath.TO_RAD, 0.0*almath.TO_RAD, 87.0*almath.TO_RAD]]
    timeLists  = [[1.0], [1.0],[1.0], [1.0],[1.0, 1.5 , 2.0, 2.5]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)

    names = ["RShoulderRoll", "RShoulderPitch", "RElbowYaw","RWristYaw", "RElbowRoll"]
    angleLists = [[0.0*almath.TO_RAD], [100.0*almath.TO_RAD],[0.0*almath.TO_RAD],[0.0*almath.TO_RAD],[3.0*almath.TO_RAD]]
    timeLists  = [[1.0], [1.0], [1.0], [1.0], [1.0]]
    isAbsolute = True
    motionProxy.closeHand("RHand")
    motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    #motionProxy.setStiffnesses("Body", 0)

def detectMarkAndMoveTo():
    markD = lookAroundForMark()
    x,y,z = NaoMarkModule.getMarkXYZ(robotIP, PORT, markD, naomarkSize)
    moveForwardY(x-.05, y)

def detectMarkAndMoveToRight():
    markD = lookAroundForMark()
    x,y,z = NaoMarkModule.getMarkXYZ(robotIP, PORT, markD, naomarkSize)
    moveForwardY(x, y-.25)

def detectMarkAndMoveToLeft():
    markD = lookAroundForMark()
    x,y,z = NaoMarkModule.getMarkXYZ(robotIP, PORT, markD, naomarkSize)
    moveForwardY(x, y +.25)
stiffnesses  = 1.0
motionProxy.setStiffnesses("Body", stiffnesses)
postureProxy.goToPosture("StandInit", 1.0)
time.sleep(1)

motionProxy.setExternalCollisionProtectionEnabled("All", False)


detectMarkAndMoveToRight()

moveForward(1)


wave()
tts.say("hello, I am robbie")
turnAround()
detectMarkAndMoveToLeft()

detectMarkAndMoveTo()
turnAround()

#motionProxy.changeAngles("HeadYaw",1, 0.1)
#print motionProxy.getAngles("HeadYaw",False)
#turnLeft90()
#print motionProxy.getAngles("HeadYaw", False)


postureProxy.goToPosture("Sit", 1.0)