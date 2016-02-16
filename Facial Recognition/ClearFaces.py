#Test code for clearing face detection database
#Mitch Deplazes
#2/16/16

from naoqi import ALProxy
import FacialRecognitionModule
import time

#IP of the Robot
IP = "10.0.0.6"
#Port Number of the Robot
PORT = 9559

FacialRecognitionModule.clearFaceDatabase(IP, PORT)

print ("Faces cleared")

