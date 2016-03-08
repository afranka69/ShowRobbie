import sys
import time

from naoqi import ALBroker
from optparse import OptionParser

NAO_IP = "10.0.0.7"

myBroker = None

class BrokerController():
    def createBroker(self):
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

    def waitToStop(self):

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print
            print "Interrupted by user, shutting down"
            myBroker.shutdown()
            sys.exit(0)