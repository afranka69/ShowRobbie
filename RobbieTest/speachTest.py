from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "10.0.0.7", 9559)
tts.say("hello i am robbie")
print tts.getAvailableVoices()