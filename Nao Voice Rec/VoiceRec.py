from naoqi import ALProxy, ALModule

class NAOVoiceRec(ALModule):
    def __init__(self, id, ip, port, wordList, callBack, wordSpotting=True, visualExpression=True, audioExpression=False):
        super(NAOVoiceRec, self).__init__(id)
        self.id = id
        self.wordCallBack = callBack;

        #create the speech recognition proxy
        self.speechRec = ALProxy("ALSpeechRecognition", ip, port)

        #set the language
        self.speechRec.setLanguage("English")
        #load the vocabulary
        self.speechRec.setVocabulary(wordList, wordSpotting)
        self.speechRec.subscribe(id)
        # configure expressions
        self.speechRec.setVisualExpression(visualExpression)
        self.speechRec.setAudioExpression(audioExpression)

        #get the ALMemory Proxy and subscribe to the events
        self.memProx = ALProxy("ALMemory")
        self.memProx.subscribeToEvent("WordRecognized", self.id, "wordRecognized")

    def __del__(self):
        self.speechRec.unsubscribe(self.id)
        self.memProx.unsubscribeToEvent("WordRecognized", self.id)

    def wordRecognized(self, event, words, id):
        self.wordCallBack(words)