from Xlib import display
from time import sleep
import math
from math import atan2, degrees, pi
import subprocess
import numpy
import random
import sys
import argparse

import colormath
from colormath.color_objects import XYZColor, sRGBColor, xyYColor, HSVColor
from colormath.color_conversions import convert_color



parser = argparse.ArgumentParser(description='Choose different patterns for the lightbar.')

parser.add_argument('-d', '--delay', dest='delay', nargs='?',
                   type=float, default=2.3, const=2.3,
                   help='Delay in seconds for each color change')

parser.add_argument('-s', '--setting', dest='setting', nargs='?',
                   type=str, default='cycle', const='cycle', choices=['random', 'cycle'],
                   help='Choose between different settings')

args = parser.parse_args()
delay = args.delay
setting = args.setting

def main():
	#run chosen setting

	subprocess.Popen("ectool lightbar seq stop", shell=True)	#stop lightbar from normal seq

	if setting == 'random':
		bounceHSV()
	elif setting == 'cycle':
		circleHSV()
	else:
		exit()	#should not be able to reach this





def pol2cart(rho, phi):
    x = rho * numpy.cos(phi)
    y = rho * numpy.sin(phi)
    return(x, y)

def setColor(hexValue):		#set LEDs to passed in hex value
	subprocess.Popen("ectool lightbar 4 " + hexValue[1:3] + ' ' + hexValue[5:] + ' ' + hexValue[3:5], shell=True)


def circleHSV():	#loop along outer edge of HSV colors
	deg = random.randint(0, 359)		#start at degree 0
	increment = .6

	while 1:
		if deg > 360: deg = 0
		c = colormath.color_objects.HSVColor(deg, 1, .9)
		r = convert_color(c, sRGBColor)
		hexColor = r.get_rgb_hex()	#get hex value for color
		setColor(hexColor)

		deg += increment

		sleep(delay)

def bounceHSV():	#bounce around the HSV circle

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
			sleep(delay)
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

			setColor(hexColor)

main()