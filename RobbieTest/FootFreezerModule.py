#Makes nao stop and move either to the left or right when the right or left foot bumper is pressed, respectively
# -*- encoding: UTF-8 -*-
import sys
import os
import time

from naoqi import ALProxy
from naoqi import ALModule

# Global variable
memory = None

stepArray = [["StepHeight", 0.015],["MaxStepX", 0.02], ["MaxStepTheta", .18]]
hit = False

class FootFreezerModule(ALModule):
    """ A simple module able to react
    to head tactile sensor events

    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALMotion for later use
        self.tts = ALProxy("ALMotion")

        # Subscribe to the MiddleTactilTouched event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("RightBumperPressed",
            "FootFreezer",
            "onRightBumperPressed")
        memory.subscribeToEvent("LeftBumperPressed",
            "FootFreezer",
            "onLeftBumperPressed")

    def onRightBumperPressed(self, *_args):
        """ This will be called each time the right foot bumper is pressed

        """
        # Unsubscribe to the event
        # to avoid repetitions
        memory.unsubscribeToEvent("RightBumperPressed",
            "FootFreezer")
        print "Hit right foot on something"
        self.tts.stopMove()

        ###############################
        # First we defined each step
        ###############################
        footStepsList = []

        #1) Sidestep to the left with your left foot
        footStepsList.append([["LLeg"], [[0.00, 0.16, 0.0]]])

        # 3) Move your right foot to your left foot
        footStepsList.append([["RLeg"], [[0.00, -0.1, 0.0]]])

        ###############################
        # Send Foot step
        ###############################
        stepFrequency = 0.8
        clearExisting = False
        self.tts.moveTo(0, .05, 0, stepArray)


        # Subscribe again to the event
        memory.subscribeToEvent("RightBumperPressed",
            "FootFreezer",
            "onRightBumperPressed")

        global hit
        hit= True

    def onLeftBumperPressed(self, *_args):
        """ This will be called each time the right foot bumper is pressed

        """
        # Unsubscribe to the event
        # to avoid repetitions
        memory.unsubscribeToEvent("LeftBumperPressed",
            "FootFreezer")
        print "Hit left foot on something"
        self.tts.stopMove()

        ###############################
        # First we defined each step
        ###############################
        footStepsList = []

        # 8) Sidestep to the right with your right foot
        footStepsList.append([["RLeg"], [[0.00, -0.16, 0.0]]])

        # 7) Move your left foot to your right foot
        footStepsList.append([["LLeg"], [[0.00, 0.1, 0.0]]])

        ###############################
        # Send Foot step
        ###############################
        self.tts.moveTo(0, -.05, 0, stepArray)

        # Subscribe again to the event
        memory.subscribeToEvent("LeftBumperPressed",
            "FootFreezer",
            "onLeftBumperPressed")

        global hit
        hit= True

    def getHit(self):
        global hit
        h = hit
        hit = False
        return h