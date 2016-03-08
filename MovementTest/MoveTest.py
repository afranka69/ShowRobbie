__author__ = 'PTTN40'

import time
from naoqi import ALProxy
from NaoMarkModule import getMarkData
from NaoMarkModule import getMarkXYZ

def main(robotIp):
    cnt = 0;
    move = False
    motionProxy = ALProxy("ALMotion", robotIp, 9559)
    postureProxy = ALProxy("ALRobotPosture", robotIp, 9559)

    postureProxy.goToPosture("StandInit", 0.5)

    while(True):
        markData = getMarkData(robotIp, 9559)

        if (markData is None or len(markData) == 0):
            motionProxy.move(0.0, 0.0, 0.0)

        else:
            xDist, yDist, zDist = getMarkXYZ(robotIp, 9559, markData, 0.15)
            print(xDist)
            if(xDist > 0.1):
                motionProxy.move(0.2, 0.0, 0.0)
                move = True
            elif(xDist <= 0.1):
                motionProxy.move(0.0, 0.0, 0.0)
                move = False


main("10.0.0.7")