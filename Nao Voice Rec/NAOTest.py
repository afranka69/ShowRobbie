from naoqi import ALProxy
from naoqi import ALBroker
from VoiceRec import NAOVoiceRec
import random

cnt = -1
ans = -1
Play = True

wordList = ["yes", "no", "test"]
guessGameWorldList = ["one","two","three","four","five","six","seven","eight","nine","ten"]

def stringToInt(str):
    if str == "one":
        return 1
    elif str == "two":
        return 2
    elif str == "three":
        return 3
    elif str == "four":
        return 4
    elif str == "five":
        return 5
    elif str == "six":
        return 6
    elif str == "seven":
        return 7
    elif str == "eight":
        return 8
    elif str == "nine":
        return 9
    elif str == "ten":
        return 10
    else:
        return -1

def initGame(tryCnt):
    global cnt
    global ans
    tts = ALProxy("ALTextToSpeech", "10.0.0.7", 9559)
    if tryCnt < 0:
        cnt = 0
        random.seed()
        indx = random.randint(0,9)
        ans = stringToInt(guessGameWorldList[indx])
        print(ans)

        tts.say("Try to guess a number between 1 and 10")

def handler(wordList):
    print wordList

def playGuessGame(wordList):
    #check if we need to start/restart the game
    global cnt
    global ans
    global Play

    print wordList

    tts = ALProxy("ALTextToSpeech", "10.0.0.7", 9559)
    initGame(cnt)
    guess = stringToInt(wordList[0])

    if(cnt > 3):
        cnt = -1
        tts.say("Sorry you have lost")
        Play = False
    elif(guess == ans):
        cnt = -1
        tts.say("You have won!")
        Play = False
    elif(guess < ans):
        cnt += 1
        tts.say("Low")
    elif(guess > ans):
        cnt += 1
        tts.say("High")
    else:
        tts.say("Sorry I did not understand you")
        return

    tts.say("Try again")
    return

ip = "10.0.0.7"
port = 9559

broker = ALBroker("pythonBroker", "0.0.0.0", 0, ip, port)

initGame(cnt)
Test = NAOVoiceRec("Test", ip, port, guessGameWorldList, playGuessGame, False, True, False)

while True:
    pass


broker.shutdown()