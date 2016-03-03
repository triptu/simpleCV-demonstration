#This is a simple demonstration of use of SimpleCV to display live from your Webcam.
#Requirements- SimpleCV and python.

from SimpleCV import *
cam=Camera()
while True:
    img=cam.getImage()
    img.show()
