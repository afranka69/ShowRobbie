#Testing file for NaoMarkModule getMark XYZ function
from naoqi import ALProxy
import NaoMarkModule

#IP of the Robot
IP = "10.0.0.6"
#Port Number of the Robot
PORT = 9559

#Get the x,y,z in meters
x, y, z = NaoMarkModule.getMarkXYZ(IP, PORT, 0.08)

#Print information
print "x " + str(x) + " (in meters)"
print "y " + str(y) + " (in meters)"
print "z " + str(z) + " (in meters)"

