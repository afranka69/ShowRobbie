#Motion code snippet for continuously centering head to a visible nao mark (tests naoMarkModule getMarkAngles function)
#Mitch Deplazes
#2/2/16

from naoqi import ALProxy
import NaoMarkModule
import time

#IP of the Robot
IP = "10.0.0.6"
#Port Number of the Robot
PORT = 9559

#create a motion proxy
motionProxy = ALProxy("ALMotion", IP, PORT)

while True:
    #Get angle of the mark
    wzCamera, wyCamera = NaoMarkModule.getMarkAngles(IP, PORT)

    #Update head postion to center naomark
    motionProxy.setStiffnesses("Body", 1.0)
    motionProxy.changeAngles("HeadYaw", wzCamera, 0.1)
    motionProxy.changeAngles("HeadPitch", wyCamera, 0.1)
    time.sleep(1)

