#@file BotFreezerTester.py
#Adapted from http://doc.aldebaran.com/1-14/dev/python/reacting_to_events.html#python-reacting-to-events
#to make Nao "freeze" when his head tactile sensors are pressed
# -*- encoding: UTF-8 -*-

#imports
from BotFreezerModule import BotFreezerModule
from NonBlockWalk import NonBlockWalk
from BrokerController import BrokerController

NAO_IP = "10.0.0.6"

# Global variable to store the BotFreezer module instance
BotFreezer = None
brokyControlly = None

def main():
    """ Main entry point

    """

    global brokyControlly
    brokyControlly = BrokerController()
    brokyControlly.createBroker()

    # Warning: BotFreezer must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global BotFreezer
    BotFreezer = BotFreezerModule("BotFreezer")

    nonBlockyWalky = NonBlockWalk()
    #During this non-blocking walk, if any head tactil
    #is pressed, the robot will stop and sit
    nonBlockyWalky.walk()

    brokyControlly.waitToStop()


if __name__ == "__main__":
    main()
