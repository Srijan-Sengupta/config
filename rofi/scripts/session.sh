if [ ! -z "$@" ]; then
	if [[ "$@" == "Lock" ]]; then
		(sleep 2 && swaylock -e -i /usr/share/backgrounds/archlinux/awesome.png) & disown
	elif [[ "$@" == "Poweroff" ]]; then
		systemctl poweroff
	elif [[ "$@" == "Suspend" ]]; then
		systemctl suspend
	elif [[ "$@" == "Reboot" ]]; then
		systemctl reboot
	elif [[ "$@" == "Hibernate" ]]; then
		systemctl hibernate
	elif [[ "$@" == "Logout" ]]; then
		loginctl terminate-session self
	fi
	exit 0
fi

echo Poweroff
echo Suspend
echo Reboot
echo Lock
echo Hibernate
echo Logout
