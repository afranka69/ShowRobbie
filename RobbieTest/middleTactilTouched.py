#Adapted from http://doc.aldebaran.com/1-14/dev/python/reacting_to_events.html#python-reacting-to-events
#to make Nao "freeze" when his head tactile sensors are pressed

#Version 1, tries to have the bot start moving, and say "Hello, you" when his middle
#tactil sensor is pressed

# -*- encoding: UTF-8 -*-


import sys
import time
import math

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "10.0.0.7"


# Global variable to store the HumanGreeter module instance
BotFreezer = None
memory = None


class BotFreezerModule(ALModule):
    """ A simple module able to react
    to head tactile sensor events

    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")

        # Subscribe to the MiddleTactilTouched event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("MiddleTactilTouched",
            "BotFreezer",
            "onMiddleTactilTouched")

    def onMiddleTactilTouched(self, *_args):
        """ This will be called each time the middle tactil is
        detected.

        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("MiddleTactilTouched",
            "BotFreezer")
        print "Saying Something"
        self.tts.say("Hello, you")

        # Subscribe again to the event
        memory.subscribeToEvent("MiddleTactilTouched",
            "BotFreezer",
            "onMiddleTactilTouched")


def main():
    """ Main entry point

    """


    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port


    # Warning: BotFreezer must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global BotFreezer
    BotFreezer = BotFreezerModule("BotFreezer")


########################################################################################
    motionProxy = ALProxy("ALMotion")
    #http://doc.aldebaran.com/2-1/dev/python/making_nao_move.html?highlight=post#making-nao-move
    postureProxy = ALProxy("ALRobotPosture")

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)
    #motionProxy.moveInit()
    #http://doc.aldebaran.com/2-1/dev/python/examples/motion/walk.html#move-to
    X = 0.3
    Y = 0.1
    Theta = math.pi/2.0
    motionProxy.post.moveTo(.5, 0, 0)
    #moveTo with post isn't a blocking call
    # Go to rest position
    postureProxy.goToPosture("Sit", 1.0)

#########################################################################################


    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)



if __name__ == "__main__":
    main()