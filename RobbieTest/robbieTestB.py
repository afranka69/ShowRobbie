import argparse
import motion
import time
import almath
import NaoMarkModule
#For Freezing Bot
from BrokerController import BrokerController
from BotFreezerModule import BotFreezerModule

from naoqi import ALModule
from naoqi import ALProxy

robotIP = "10.0.0.7"
PORT = 9559
postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

lifeProxy = ALProxy("ALAutonomousLife", robotIP, PORT)
tts = ALProxy("ALTextToSpeech", robotIP, PORT)
motionProxy = ALProxy("ALMotion", robotIP, PORT)
curAngle = 0

# Global variables to store the module instances
BotFreezer = None
cmModule = None

class customMotions(ALModule):
    """A module for all the motions defined by the Senior Design team"""



    def turnRight90(self):
        customMotions.motionProxy.moveInit()
        time.sleep(1)
        global curAngle
        motionProxy.moveTo(0, 0, curAngle -1.57)
        curAngle += -1.57

    def lookAround(self):
        motionProxy.moveInit()
        time.sleep(1)

        names = "HeadYaw"
        angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
        times      = [1.0,  2.0, 3.0,  4.0, 5.0]
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

    def lookTo(self, angle):
        motionProxy.moveInit()
        time.sleep(1)

        motionProxy.changeAngles("HeadYaw", angle,.1)

    def lookAroundForMark(self):
        motionProxy.moveInit()
        time.sleep(1)

        names = "HeadYaw"
        markFound = False
        first = True
        angleLists = .25
        back = False
        markData = NaoMarkModule.getMarkData(robotIP, PORT)

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

            times = .05
            if(first):
                times = 2.0
            print times
            isAbsolute = True
            motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

            markData = NaoMarkModule.getMarkData(robotIP, PORT)

            if(not (markData is None or len(markData) ==0)):
                markFound =True
            first = False

        return markData

    def turnToHeadStraight(self,markData):
         motionProxy.moveInit()
         time.sleep(1)
         global curAngle

         deltaAngle,dontcare = NaoMarkModule.getMarkAngles(markData)

         angle = motionProxy.getAngles("HeadYaw",False)
         print angle[0]

         motionProxy.moveTo(0, 0, angle[0])
         print "Moved to head straight"


    def detectMarkWalkStraight(self):
        markD =  customMotions.lookAroundForMark()
        x,y,z = NaoMarkModule.getMarkXYZ(robotIP, PORT, markD, .08)
        customMotions.turnToHeadStraight(markD)
        customMotions.detectMarkAndMoveTo()


    def turnLeft90(self):
        motionProxy.moveInit()
        time.sleep(1)
        global curAngle
        motionProxy.moveTo(0, 0, curAngle + 1.57)
        curAngle += 1.57

    def turnAround(self):
        motionProxy.moveInit()
        time.sleep(1)
        global curAngle
        motionProxy.post.moveTo(0,0, curAngle - 3.14)
        curAngle += -3.14

    def moveForward(self,distance):
        motionProxy.moveInit()
        time.sleep(1)
        motionProxy.moveTo(distance, 0, 0)

    def moveForwardY(self,distance, y):
        motionProxy.moveInit()
        time.sleep(1)
        motionProxy.moveTo(distance, y, 0)

    def moveStrafe(self,distance, theta):
        motionProxy.moveInit()
        time.sleep(1)
        motionProxy.moveTo(distance, 0, theta)

    def wave(self):
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
      #  motionProxy.setStiffnesses("Body", 0)

    def detectMarkAndMoveTo(self):
        markD = customMotions.lookAroundForMark()
        x,y,z = NaoMarkModule.getMarkXYZ(robotIP, PORT, markD, .08)
        customMotions.moveForwardY(x, y)



def main():
    """ Main entry point
    """

    ########################FOR FREEZING BOT#######################
    global brokyControlly
    brokyControlly = BrokerController()
    brokyControlly.createBroker()

    # Warning: BotFreezer must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global BotFreezer
    BotFreezer = BotFreezerModule("BotFreezer")

    global cmModule
    cmModule = customMotions("cmModule")
    cm = ALProxy("cmModule")
    ###################FOR FREEZING BOT############################

    stiffnesses  = 1.0
    motionProxy.setStiffnesses("Body", stiffnesses)
    postureProxy.goToPosture("StandInit", 1.0)
    time.sleep(1)

    motionProxy.setExternalCollisionProtectionEnabled("All", False)

    #nonBlocky also has to have a post in it, along with
    #the walk commands INSIDE "NonBlockWalk2.py", if wait()
    #is going to work correctly




    #Print information
    # print "x " + str(x) + " (in meters)
    # print "y " + str(y) + " (in meters)"
    # print "z " + str(z) + " (in meters)"

    #turnAround()
    #detectMarkAndMoveTo()

    #id = customMotions.detectMarkAndMoveTo()


    #customMotions.moveForwardY(0, -.25)
    #customMotions.detectMarkAndMoveTo()
    #customMotions.wave()
    #tts.say("Hello I am Robbie")

    id = cm.post.detectMarkAndMoveTo()
    cm.wait(id, 0)

    id = cm.post.moveForwardY(0, -.25)
    cm.wait(id, 0)

    id = cm.post.detectMarkAndMoveTo()
    cm.wait(id, 0)

  #  id = cm.post.wave()
  #  cm.wait(id, 0)

    id = cm.post.turnAround()
    cm.wait(id, 0)

    id = cm.post.detectMarkAndMoveTo()
    cm.wait(id, 0)

    id = cm.post.detectMarkAndMoveTo()
    cm.wait(id, 0)

    id = cm.post.turnAround()
    cm.wait(id, 0)






    #time.sleep(2)
    #tts.say("I am turned around")
    #customMotions.detectMarkAndMoveTo()
    #customMotions.detectMarkAndMoveTo()
    #customMotions.turnAround()


    #motionProxy.changeAngles("HeadYaw",1, 0.1)
    #print motionProxy.getAngles("HeadYaw",False)
    #turnLeft90()
    #print motionProxy.getAngles("HeadYaw", False)


    postureProxy.goToPosture("Sit", 1.0)

    #################FOR FREEZING BOT###########################
    # end broker to stop
    brokyControlly.waitToStop()
    #################FOR FREEZING BOT###########################

if __name__ == "__main__":
    main()