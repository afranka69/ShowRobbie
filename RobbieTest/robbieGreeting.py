#TEsts the searching for nao marks with the ability to stop him by touching his head tactils


from motions import customMotions
import time
from naoqi import ALProxy
#For Freezing Bot
from BrokerController import BrokerController
from BotFreezerModule import BotFreezerModule
from FootFreezerModule import FootFreezerModule

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
FootFreezer = None


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
    #global FootFreezer
    #FootFreezer = FootFreezerModule("FootFreezer")
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
    id = cm.post.detectMarkAndMoveTo75(107)
    cm.wait(id,0)

    id = cm.post.turnRight90()
    cm.wait(id,0)

    id = cm.post.lookAroundForMark(114)
    cm.wait(id,0)

    id = cm.post.wave()
    cm.wait(id,0)
    tts.say("Hello, I am Robbie. I'm a NAO robot. I'm designed and manufactured by the Aldebaan company in France, but all of my present behaviors have been programmed as part of a Senior Software Engineering project")
    tts.say("There's very little I can do without the programs that have designed and constructed by the Senior Software Engineering students here at Montana Tech. I'm afraid that programming me is not easy, but these students have been well equiped by their education here at Tech to deal with complex problems.")


    id = cm.post.fistBump()
    cm.wait(id,0)

    id = cm.post.turnRight50()
    cm.wait(id,0)
    id = cm.post.detectMarkSearch(64, "l")
    cm.wait(id,0)

    id = cm.post.moveForward(.2)
    cm.wait(id,0)

    id = cm.post.detectMarkSearchForward(68)
    cm.wait(id,0)
    id = cm.post.turnAround()
    cm.wait(id,0)

    #id = cm.post.turnAround()
    #cm.wait(id, 0)
    #time.sleep(2)
    #tts.say("I am turned around")



    postureProxy.goToPosture("Sit", 1.0)

    #################FOR FREEZING BOT###########################
    # end broker to stop
    brokyControlly.waitToStop()
    #################FOR FREEZING BOT###########################

if __name__ == "__main__":
    main()