from Xlib import display
from time import sleep
import math
from math import atan2, degrees, pi
import subprocess
import numpy
import random

import colormath
from colormath.color_objects import XYZColor, sRGBColor, xyYColor, HSVColor
from colormath.color_conversions import convert_color


subprocess.Popen("echo lol | sudo -S ectool lightbar seq stop", shell=True)	#stop lightbar from normal seq

def pol2cart(rho, phi):
    x = rho * numpy.cos(phi)
    y = rho * numpy.sin(phi)
    return(x, y)


startX = -1
startY = 0

xInc = 0.01  #Amount x value will change each tick

currX = 0
currY = 0

#  H = angle,	S = distance from center

while 1:
	deg = random.randint(0, 360)	#calculate where on circle to move to
	endX, endY = pol2cart(1, math.radians(deg))	#coord to move line to
	slope = (startY - endY) / (startX - endX)

	dX = math.copysign(xInc, slope)

	currX = startX
	currY = startY
	while 1:	#move current color until position is at or past endX
		sleep(.55)
		currX += dX
		currY += (slope * xInc)

		distCenter = math.hypot(currX-0, currY-0)

		if distCenter > .99: #check if outside of unit circle 
			startX = endX
			startY = endY
			break	

		dx = currX - 0
		dy = currY - 0
		rads = atan2(-dy,dx)
		rads %= 2*pi
		hValue = degrees(rads)

		c = colormath.color_objects.HSVColor(hValue, distCenter, .9)
		r = convert_color(c, sRGBColor)
		hexColor = r.get_rgb_hex()

		subprocess.Popen("echo lol | sudo -S ectool lightbar 4 " + hexColor[1:3] + ' ' + hexColor[5:] + ' ' + hexColor[3:5], shell=True)











