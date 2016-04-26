from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "10.0.0.7", 9559)
tts.say("Hello, I am Robbie. I'm a NAO robot. I'm designed and manufactured by the Aldebaan company in France, but all of my present behaviors have been programmed as part of a Senior Software Engineering project")
tts.say("There's very little I can do without the programs that have designed and constructed by the Senior Software Engineering students here at Montana Tech. I'm afraid that programming me is not easy, but these students have been well equiped by their education here at Tech to deal with complex problems.")

