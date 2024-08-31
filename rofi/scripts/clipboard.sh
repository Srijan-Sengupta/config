if [ ! -z "$@" ]; then
	echo "$@"|cliphist decode|wl-copy
	exit 0
fi

cliphist list
