#@file BrokerController.py
#This class can be used for its methods createBroker()
#and waitToStop(). A living broker is necessary for scripts that
#have the robot respond to events, such as head tactil presses.
#So, in BotFreezerTester.py, this class is imported, made a
#proxy of, and used to create a broker and keep it going
#until BotFreezerTester's main() is stopped.

import sys
import time

from naoqi import ALBroker
from optparse import OptionParser

NAO_IP = "10.0.0.6"

myBroker = None

class BrokerController():

    #Create a broker
    def createBroker(self):

        #Still not sure exactly what pip and pport do, but
        #they allow a program not to use the actual ip and port
        #numbers of the robot
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
        global myBroker
        myBroker = ALBroker("myBroker",
           "0.0.0.0",   # listen to anyone
           0,           # find a free port and use it
           pip,         # parent broker IP
           pport)       # parent broker port

    #Keep the broker alive until further notice (KeyboardInterrupt)
    def waitToStop(self):

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print
            print "Interrupted by user, shutting down"
            myBroker.shutdown()
            sys.exit(0)
