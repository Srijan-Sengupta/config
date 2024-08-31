if [ ! -z "$@" ]; then
	PROCESS=$@
	PROCESS_PID=$(echo $PROCESS|awk '{print $1}')
	kill $PROCESS_PID
	notify-send "Killed $PROCESS"
	unset PROCESS PROCESS_PID
	exit 0
fi

ps -u $USER,nobody,libvirt-qemu --no-headers -o pid,atime,user,args
