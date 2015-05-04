#!/bin/bash
#Adjust keyboard backlight brighter or dimmer based on passed in parameters
#brightness file is located at /sys/class/leds/chromeos::kbd_backlight/brightness

currValue=$(cat /sys/class/leds/chromeos::kbd_backlight/brightness)
if [ "$1" = "inc" ] && [ $currValue -ne 100 ]; then
	newValue=$(( $currValue + 25 ))
	execLine='echo -n '$newValue' > /sys/class/leds/chromeos::kbd_backlight/brightness'
	echo lol | sudo -S bash -c "$execLine"
elif [ "$1" = "dec" ]  && [ $currValue -ne 0 ]; then
	newValue=$(( $currValue - 25 ))
	execLine='echo -n '$newValue' > /sys/class/leds/chromeos::kbd_backlight/brightness'
	echo lol | sudo -S bash -c "$execLine"
fi