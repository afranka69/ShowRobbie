from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "10.0.0.7", 9559)
tts.say("hello puny humans. I am Robbie. I am programmed by the CS and SE students here at Montana Tech")
print tts.getAvailableVoices()