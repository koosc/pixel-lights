from Xlib import display
from time import sleep
import math
from math import atan2, degrees, pi
import subprocess

import colormath
from colormath.color_objects import XYZColor, sRGBColor, xyYColor, HSVColor
from colormath.color_conversions import convert_color

#2560
#1700
#3073

centerX = 1280
centerY = 850
redMax = 2560  #x
greenMax = 3073	#z
blueMax = 1700	#y

subprocess.Popen("echo lol | sudo -S ectool lightbar seq stop", shell=True)

def mousepos():
    #"""mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]



while 1:
	sleep(0.15)
	x, y = mousepos()
	distCenter = math.hypot(x-centerX, y-centerY)
	# print(distCenter)
	sValue = distCenter/1536

	dx = x - centerX
	dy = y - centerY
	rads = atan2(-dy,dx)
	rads %= 2*pi
	hValue = degrees(rads)


	c = colormath.color_objects.HSVColor(hValue, sValue, .9)
	r = convert_color(c, sRGBColor)
	hexColor = r.get_rgb_hex()

	# print(hexColor)

	# subprocess.Popen("echo lol | sudo -S ectool lightbar 4 " + redValue + ' ' + greenValue + ' ' + blueValue, shell=True)

	subprocess.Popen("echo lol | sudo -S ectool lightbar 4 " + hexColor[1:3] + ' ' + hexColor[5:] + ' ' + hexColor[3:5], shell=True)
