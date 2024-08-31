#!/bin/bash
UPDATES=$(checkupdates|wc --lines)

if [ $UPDATES -le 0 ]; then
	echo ""
else
	echo "{\"text\":\" $UPDATES\", \"tooltip\":\"$UPDATES package update available click to update\"}"
fi
