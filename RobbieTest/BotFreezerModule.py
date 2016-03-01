#@file BotFreezerModule.py
#Adapted from http://doc.aldebaran.com/1-14/dev/python/reacting_to_events.html#python-reacting-to-events
#to make Nao "freeze" when any of his head tactile sensors are pressed
# -*- encoding: UTF-8 -*-

#imports
from naoqi import ALProxy
from naoqi import ALModule

# Global variable
memory = None

class BotFreezerModule(ALModule):
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
        memory.subscribeToEvent("FrontTactilTouched",
            "BotFreezer",
            "onTactilTouched")
        memory.subscribeToEvent("MiddleTactilTouched",
            "BotFreezer",
            "onTactilTouched")
        memory.subscribeToEvent("RearTactilTouched",
            "BotFreezer",
            "onTactilTouched")

    def onTactilTouched(self, *_args):
        """ This will be called each time any head tactil is
        detected.

        """
        # Unsubscribe to the event
        # to avoid repetitions
        memory.unsubscribeToEvent("FrontTactilTouched",
            "BotFreezer")
        memory.unsubscribeToEvent("MiddleTactilTouched",
            "BotFreezer")
        memory.unsubscribeToEvent("RearTactilTouched",
            "BotFreezer")
        print "Stopping walk"
        self.tts.stopMove();
        self.tts.rest();

        # Subscribe again to the event
        memory.subscribeToEvent("FrontTactilTouched",
            "BotFreezer",
            "onTactilTouched")
        memory.subscribeToEvent("MiddleTactilTouched",
            "BotFreezer",
            "onTactilTouched")
        memory.subscribeToEvent("RearTactilTouched",
            "BotFreezer",
            "onTactilTouched")
