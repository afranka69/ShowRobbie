#File for test NaoMarkModule getMarkNumber function

from naoqi import ALProxy
import NaoMarkModule

#IP of the Robot
IP = "10.0.0.7"
#Port Number of the Robot
PORT = 9559

#Make proxy to speech
speechProxy = ALProxy("ALTextToSpeech", IP, PORT)

markData = NaoMarkModule.getMarkData(IP, PORT)

while((markData is None or len(markData) ==0)):
    markData = NaoMarkModule.getMarkData(IP, PORT)

#Get mark number
markID = NaoMarkModule.getMarkNumber(markData)

#Say mark number with speech
speechProxy.say("The Nao Mark I see is " + str(markID))
print markID
