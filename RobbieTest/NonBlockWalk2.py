#Robbie walks forward without blocking until done walking.
#None-blocking walk command allows other functions to run at the
#same time including the function to stop moving and sit down
#if Robbie's head tactils are pressed (BotFreezerModule.py)

import time
from naoqi import ALProxy
from naoqi import ALModule

#Define the NonBlockWalk class
class NonBlockWalk2(ALModule):
    """ A simple module able to walk without blocking"""

    def walk(self):
        motionProxy = ALProxy("ALMotion")
        #http://doc.aldebaran.com/2-1/dev/python/making_nao_move.html?highlight=post#making-nao-move
        postureProxy = ALProxy("ALRobotPosture")

        # Wake up robot
        motionProxy.wakeUp()

        # Send robot to Stand Init
        postureProxy.goToPosture("StandInit", 1.0)
        time.sleep(1)
        motionProxy.setExternalCollisionProtectionEnabled("All", False)
        motionProxy.moveInit()
        #http://doc.aldebaran.com/2-1/dev/python/examples/motion/walk.html#move-to
        motionProxy.post.moveTo(0.5, 0, 0)
        #moveTo with post isn't a blocking call
        # Go to rest position

        postureProxy.goToPosture("Sit", 1.0)