#Adapted from http://doc.aldebaran.com/1-14/dev/python/reacting_to_events.html#python-reacting-to-events
#to make Nao "freeze" when his head tactile sensors are pressed
# -*- encoding: UTF-8 -*-

#########################NEEDED FOR FREEZING BOT#####################
from BrokerController import BrokerController
from BotFreezerModule import BotFreezerModule
from naoqi import ALProxy
#################END NEEDED FOR FREEZING BOT##########################

##################PROGRAM SPECIFIC MODULE IMPORTS#####################
from NonBlockWalk2 import NonBlockWalk2

#global variables for program specific module imports
nonBlockyWalky = None
###############END PROGRAM SPECIFIC MODULE IMPORTS####################

#NAO IP address
NAO_IP = "10.0.0.7"

################NEEDED FOR FREEZING BOT###############################
# Global variable to store the BotFreezer module instance
brokyControlly = None
BotFreezer = None
##########END NEEDED FOR FREEZING BOT#################################

def main():
    """ Main entry point

    """

################MAIN() CODE FOR FREEZING BOT#############################
    global brokyControlly
    brokyControlly = BrokerController()
    brokyControlly.createBroker()

    # Warning: BotFreezer must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global BotFreezer
    BotFreezer = BotFreezerModule("BotFreezer")
##########END MAIN() CODE FOR FREEZING BOT################################



#############################PROGRAM SPECIFIC ############################
    #Program specific proxies
    speechProxy = ALProxy("ALTextToSpeech")
    global nonBlockyWalky
    nonBlockyWalky = NonBlockWalk2("nonBlockyWalky")
    nonBlocky = ALProxy("nonBlockyWalky")

    #nonBlocky also has to have a post in it, along with
    #the walk commands INSIDE "NonBlockWalk2.py", if wait()
    #is going to work correctly
    id = nonBlocky.post.walk()
    nonBlocky.wait(id, 0)
    speechProxy.say("I have arrived.")
############################END PROGRAM SPECIFIC############################



################MAIN() CODE FOR FREEZING BOT################################
    brokyControlly.waitToStop()
###########END MAIN() CODE FOR FREEZING BOT#################################


if __name__ == "__main__":
    main()