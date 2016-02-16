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
    foundFace = False
    faceData = FacialRecognitionModule.getFaceData(IP, PORT)

    while(not foundFace):
        #Get data until face is found
        while (faceData is None or len(faceData) == 0):
            print ("looking for face")
            faceData = FacialRecognitionModule.getFaceData(IP, PORT)

        if(FacialRecognitionModule.getFaceConfidince(faceData) > 0.4):
            foundFace = True
        else:
            print ("conf found")
            faceData = FacialRecognitionModule.getFaceData(IP, PORT)


    faceName = FacialRecognitionModule.getFaceName(faceData)


    #Make proxy to speech
    speechProxy = ALProxy("ALTextToSpeech", IP, PORT)
    speechProxy.say("Hello " + str(faceName))

    time.sleep(1)
