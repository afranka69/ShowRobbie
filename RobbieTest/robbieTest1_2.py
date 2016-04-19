#TEsts the searching for nao marks with the ability to stop him by touching his head tactils


from robbieTest2_0 import customMotions
import time
from naoqi import ALProxy
#For Freezing Bot
from BrokerController import BrokerController
from BotFreezerModule import BotFreezerModule

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


    id = cm.post.detectMarkAndMoveTo75Right(80)
    cm.wait(id,0)

    id = cm.post.moveForwardY(0,-.2)
    cm.wait(id,0)
    id = cm.post.detectMarkAndMoveTo75(64)
    cm.wait(id,0)

    id = cm.post.turnRight90()
    cm.wait(id,0)

    id = cm.post.lookAroundForMark(114)
    cm.wait(id,0)

    id = cm.post.wave()
    cm.wait(id,0)
    tts.say("Hello, I am Robbie.")

    id = cm.post.turnRight50()
    cm.wait(id,0)
    id = cm.post.detectMarkSearch(64, "l")
    cm.wait(id,0)
    id = cm.post.detectMarkAndMoveTo(68)
    cm.wait(id,0)
    id = cm.post.turnAround()
    cm.wait(id,0)

    #id = cm.post.turnAround()
    #cm.wait(id, 0)
    #time.sleep(2)
    #tts.say("I am turned around")

    id = cm.post.fistBump()
    cm.wait(id,0)

    postureProxy.goToPosture("Sit", 1.0)

    #################FOR FREEZING BOT###########################
    # end broker to stop
    brokyControlly.waitToStop()
    #################FOR FREEZING BOT###########################

if __name__ == "__main__":
    main()