#!/bin/bash

# You can call this script like this:
# $./volume.sh up
# $./volume.sh down
# $./volume.sh mute

function get_volume {
	pactl list sinks|grep Volume|grep front-|awk '{print $5}'|sed 's/%//'
}

function is_mute {
	pactl list sinks |grep Mute|awk '{print $2}'|grep yes
}

function send_notification {
    volume=`get_volume`
    # Make the bar with the special character ─ (it's not dash -)
    # https://en.wikipedia.org/wiki/Box-drawing_character
    #bar=$(seq -s "─" $(($volume / 5)) | sed 's/[0-9]//g')
    # Send the notification
    dunstify -h string:x-canonical-private-synchronous:audio "    $volume%" -h int:value:$volume
}

case $1 in
    up)
	# Set the volume on (if it was muted)
	pactl set-sink-mute 0 false > /dev/null
	# Up the volume (+ 5%)
	pactl set-sink-volume 0 +5% > /dev/null
	canberra-gtk-play -i audio-volume-change -d "changeVolume" > /dev/null &
	send_notification
	
	;;
    down)
	pactl set-sink-mute 0 false > /dev/null
	pactl set-sink-volume 0 -5% > /dev/null
	canberra-gtk-play -i audio-volume-change -d "changeVolume" > /dev/null &
	send_notification
	;;
    mute)
    	# Toggle mute
	pactl set-sink-mute 0 toggle > /dev/null
	if is_mute ; then
	    dunstify -h string:x-canonical-private-synchronous:audio "🔇  Muted"
	else
	    send_notification
	    canberra-gtk-play -i audio-volume-change -d "changeVolume" >/dev/null &
	fi
	;;
esac
