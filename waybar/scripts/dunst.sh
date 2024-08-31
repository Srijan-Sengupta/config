#!/bin/bash

COUNT=$(dunstctl count waiting)
ENABLED=
DISABLED=
if [ $COUNT != 0 ]; then 
	DISABLED=" $COUNT"
	ENABLED=" $COUNT"
fi

if dunstctl is-paused | grep -q "false" ; then 
	echo "{\"text\":\"$ENABLED\",\"tooltip\":\"Notifications Enabled\"}"; 
else 
	echo "{\"text\":\"$DISABLED\",\"tooltip\":\"DND mode on\"}";
fi

