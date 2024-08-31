if [ ! -z "$@" ]; then
	echo "$@"|cliphist delete
fi

cliphist list
