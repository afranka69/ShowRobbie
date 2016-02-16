#Test code for saying faces that robbie sees
#Mitch Deplazes
#2/16/16

from naoqi import ALProxy
import FacialRecognitionModule
import time

#IP of the Robot
IP = "10.0.0.6"
#Port Number of the Robot
PORT = 9559



while(True):
    #get a face
    face = FacialRecognitionModule.getFaceName(IP, PORT)

    #wait until face is found
    while (face[1] == "null"):
        face = FacialRecognitionModule.getFaceName(IP,PORT)
        print ("Face not found")

    if(face[0] > 0.4):
        #Make proxy to speech
        speechProxy = ALProxy("ALTextToSpeech", IP, PORT)
        speechProxy.say("Hello " + str(face[1]))

    time.sleep(1)
