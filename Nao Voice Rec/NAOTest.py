from naoqi import ALProxy
from naoqi import ALBroker
from VoiceRec import NAOVoiceRec

wordList = ["yes", "no", "test"]
ip = "10.0.0.7"
port = 9559

broker = ALBroker("pythonBroker", "0.0.0.0", 0, ip, port)

Test = NAOVoiceRec("Test", ip, port, wordList, )
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

broker.shutdown()