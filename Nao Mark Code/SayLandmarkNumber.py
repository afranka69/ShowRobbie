#File for test NaoMarkModule getMarkNumber function

from naoqi import ALProxy
import NaoMarkModule

#IP of the Robot
IP = "10.0.0.6"
#Port Number of the Robot
PORT = 9559

#Make proxy to speech
speechProxy = ALProxy("ALTextToSpeech", IP, PORT)

#Get mark number
markID = NaoMarkModule.getMarkNumber(IP, PORT)

#Say mark number with speech
speechProxy.say("The Nao Mark I see is " + str(markID))
