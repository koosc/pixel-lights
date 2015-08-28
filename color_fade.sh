#!/bin/bash
#Automatically turn color to fading when charger is plugged in

lightFast=0

ectool lightbar seq stop
python3 /home/chris/pixel/pixel-lights/color_fade.py &
    RUNNING_PID=$!

while true
do
	on_ac_power
    if [ "$?" -eq 0 ] && [ "$lightFast" -eq 0 ]	#turn light script on if on ac power
    then
    	sleep 12	#wait for normal power seq to finish in cast it just turned on
        sudo kill -KILL "$RUNNING_PID"   #end current script running
    	sudo ectool lightbar seq stop	#Ensure default seq ia not running
    	python3 /home/chris/pixel/pixel-lights/color_fade.py -d .15 &
			RUNNING_PID=$!
		lightFast=1
    elif [ "$lightFast" -eq 1 ]; then	#kill script if disconnected
    	on_ac_power
    	if [ "$?" -eq 1 ]; then
	    	sudo kill -KILL "$RUNNING_PID"
	    	lightFast=0
	    	# sudo ectool lightbar seq run	#set lightbar back to normal colors
            python3 /home/chris/pixel/pixel-lights/color_fade.py &
                RUNNING_PID=$!
	    fi
    fi

    sleep 90 	#Check again in 90 seconds
done
