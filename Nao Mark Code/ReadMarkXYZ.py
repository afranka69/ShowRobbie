#Testing file for NaoMarkModule getMark XYZ function
from naoqi import ALProxy
import NaoMarkModule

#IP of the Robot
IP = "10.0.0.7"
#Port Number of the Robot
PORT = 9559

#Get the x,y,z in meters
markData = NaoMarkModule.getMarkData(IP, PORT)

#Get data until face is found
while (markData is None or len(markData) == 0):
    markData = NaoMarkModule.getMarkData(IP, PORT)

x, y, z = NaoMarkModule.getMarkXYZ(IP, PORT, markData, 0.04)

#Print information
print "x " + str(x) + " (in meters)"
print "y " + str(y) + " (in meters)"
print "z " + str(z) + " (in meters)"

