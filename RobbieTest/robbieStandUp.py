import argparse
import motion
import time
import almath
from naoqi import ALProxy
robotIP = "10.0.0.6"
PORT = 9559


postureProxy = ALProxy("ALRobotPosture", "10.0.0.7", 9559)
postureProxy.goToPosture("StandInit", 1.0)
