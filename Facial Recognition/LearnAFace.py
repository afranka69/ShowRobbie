#Test code for learning a face
#Mitch Deplazes
#2/16/16

from naoqi import ALProxy
import FacialRecognitionModule
import time

#IP of the Robot
IP = "10.0.0.6"
#Port Number of the Robot
PORT = 9559

while (FacialRecognitionModule.learnFace(IP,PORT,"Mack")):
    print ("face not learned")
print ("face learned")