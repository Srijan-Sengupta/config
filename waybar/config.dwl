// vim: ft=jsonc
{
	"layer": "top",
	"position": "top",
	//"gtk-layer-shell": false,
	//"margin-bottom":5,
	//"margin-top":5,
	//"margin-left": 5,
	//"margin-right": 5,
	"modules-left": [
		"custom/launcher",
		"custom/dwl",
		"custom/title"
	],
	"modules-center": [
		"custom/notification",
		"clock",
		"custom/updates",
		"tray"
	],
	"modules-right": [
		"battery",
		"backlight",
		"cpu",
		"memory",
		"pulseaudio",
		"network",
		"keyboard-state",
		"idle_inhibitor"
	],
	"keyboard-state": {
		"numlock": true,
		"capslock": true,
		"format": "{name} {icon}",
		"format-icons": {
			"locked": "",
			"unlocked": ""
		}
	},
	"cpu": {
		"format": "{usage:>3}% {icon0} {icon1} {icon2} {icon3} ",
		"format-icons": [
			"▁",
			"▂",
			"▃",
			"▄",
			"▅",
			"▆",
			"▇",
			"█"
		],
		"interval": 1,
		"on-click": "footclient -T Usage -e btop"
	},
	"memory": {
		"interval": 1,
		"format": "{used:0.2f}G  {swapUsed:0.2f}G ",
		"on-click": "footclient -T Usage -e btop"
	},
	"network": {
		"format": "{ifname}",
		"format-wifi": "",
		"format-ethernet": "{ipaddr}/{cidr}",
		"format-disconnected": "No Internet",
		"tooltip-format": "{ifname} via {gwaddr} ",
		"tooltip-format-wifi": "{essid} ({signalStrength}%) ",
		"tooltip-format-ethernet": "{ifname} ",
		"tooltip-format-disconnected": "Disconnected",
		"on-click": "footclient -T 'NetWork Manager'-e nmtui"
	},
	"pulseaudio": {
		"format": "{volume}% {icon} {format_source}",
		"format-bluetooth": "{volume}% {icon} {format_source}",
		"format-bluetooth-muted": "婢 {icon} {format_source}",
		"format-muted": "婢 {format_source}",
		"format-source": "{volume}% ",
		"format-source-muted": "婢",
		"format-icons": {
			"headphone": "",
			"hands-free": "",
			"headset": "",
			"phone": "",
			"portable": "",
			"car": "",
			"default": [
				"",
				"",
				"墳",
				""
			]
		},
		"on-click": "footclient -T 'Audio Control' -e alsamixer -V all"
	},
	"backlight": {
		"device": "intel_backlight",
		"format": "{percent}% {icon}",
		"format-icons": [
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			""
		],
		"on-click": ""
	},
	"wlr/taskbar": {
		"format": "{icon}",
		"icon-size": 30,
		"tooltip-format": "{title}",
		"on-click": "minimize-raise",
		"on-click-middle": "close"
	},
	"idle_inhibitor": {
		"format": "{icon}",
		"format-icons": {
			"activated": "",
			"deactivated": "⏾"
		},
		"on-click": ""
	},
	"clock": {
		"on-click": "",
		"interval": 1,
		"format": "{:%I:%M:%OS %p}",
		"tooltip-format": "<big>{:%Y %B}</big>\n<tt><small>{calendar}</small></tt>",
		"format-alt": "{:%d-%m-%Y}"
	},
	"battery": {
		"on-click": "",
		"states": {
			"good": 95,
			"warning": 20,
			"critical": 15
		},
		"format": "{capacity}% {icon}",
		"format-charging": "{capacity}% ", //",
		"format-plugged": "{capacity}% ",
		"format-alt": "{time} {icon}",
		// "format-good": "", // An empty format will hide the module
		//"format-full": "{capacity}% !!!",
		"format-icons": [
			"",
			"",
			"",
			"",
			""
		]
	},
	"custom/launcher": {
		"on-click": "sh ~/.config/waybar/scripts/launcher.sh",
		"format": "/",
		"tooltip": false
		//"tooltip-format": "Start here"
	},
	"custom/notification": {
		"exec": "~/.config/waybar/scripts/dunst.sh",
		"on-click-right": "dunstctl set-paused toggle",
		"on-click": "dunstctl history-pop",
		"on-click-middle": "dunstctl close-all",
		"restart-interval": 2,
		"return-type": "json"
	},
	"custom/updates": {
		"exec": "~/.config/waybar/scripts/updates.sh",
		"on-click": "footclient -T Updates -e sudo pacman -Syu",
		"on-click-right": "",
		"restart-interval": 3600,
		"return-type": "json",
		"exec-on-event": true
	},
	"tray": {
		"icon-size": 21,
		"spacing": 10
	},
	"custom/dwl": {
		"exec": "sh ~/.config/waybar/scripts/dwlbar.sh",
		"format": " {}",
		"tooltip": false
	},
	"custom/title": {
		"exec":"sh ~/.config/waybar/scripts/dwlbar.sh title",
		"format": "{}",
		"tooltip":false
	}
}
