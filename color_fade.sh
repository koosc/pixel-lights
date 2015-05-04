#!/bin/bash
#Automatically turn color to fading when charger is plugged in

lightOn=0
while true
do
	on_ac_power
    if [ "$?" -eq 0 ] && [ "$lightOn" -eq 0 ]	#turn light script on if on ac power
    then
    	sleep 12	#wait for normal power seq to finish
    	sudo ectool lightbar seq stop	#stop default seq
    	python3 /home/chris/pixel/pixel-lights/color_fade.py &
		PID1=$!
		lightOn=1
    elif [ "$lightOn" -eq 1 ]; then	#kill script if disconnected
    	on_ac_power
    	if [ "$?" -eq 1 ]; then
	    	kill -KILL "$PID1"
	    	lightOn=0
	    	sudo ectool lightbar seq run	#set lightbar back to normal colors
	    fi
    fi

    sleep 90 	#Check again in 90 seconds
done
