#!/usr/bin/sh

#declare layout, activetags, selectedtags, urgenttags
#readonly fname="$HOME"/.cache/dwltags-wayland
fgcolor="#BD93F9"
bgcolor="#21222C"
readonly fname=/tmp/dwltags-$USER
tagname=( "1" "2" "3" "4" "5" "6" "7" "8" "9" ) 
tags=$(seq 0 8)
monitor="${1}"

_setup(){
	layout="$(grep 'layout' $fname| tail -n1|cut -d ' ' -f 3 )"
	activetags="$(grep 'tags' $fname|tail -n1| cut -d ' ' -f 3 )"
	selectedtags="$(grep 'tags' $fname|tail -n1| cut -d ' ' -f 4 )"
	urgenttags="$(grep 'tags' $fname|tail -n1| cut -d ' ' -f 6 )"
}
_loop(){
	status="|"
	for i in $tags;do
		unset statpart
		statpart=${tagname[i]}
		mask=$((1<<i))	
		if (( ${activetags} & mask )) 2>/dev/null; then statpart+='*' ; fi
		if (( ${urgenttags} & mask )) 2>/dev/null; then statpart="[$statpart]" ; fi
		if (( ${selectedtags} & mask )) 2>/dev/null; then 
			statpart="<span bgcolor='$bgcolor'><span fgcolor='$fgcolor'><b> $statpart </b></span></span>" ;
			status+="$statpart|"
		else
			status+=" $statpart |"
		fi		
		unset mask,statpart
	done
	status+=" $layout"
	echo $status
#	echo $activetags $selectedtags $urgenttags
}
if [[ title == "$@" ]]; then
	while [[ -n "$(pgrep waybar)" ]]; do
		title=`grep 'title' $fname| sed s/\"/“/g |sed 's/<//'|sed 's/>//'|tail -n1|cut -c 13-28`
		echo "$title"
		inotifywait -t 300 -qqe modify $fname
	done
else
	while [[ -n "$(pgrep waybar)" ]]; do
		_setup
		_loop
		inotifywait -qqe modify -t 300 $fname
	done
fi
