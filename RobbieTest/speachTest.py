from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "10.0.0.7", 9559)
tts.say("Hello I am Robbie. I am programmed by the SE students @ Montana Tech")
