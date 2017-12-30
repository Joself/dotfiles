#!/bin/bash

if [ "$(playerctl status)" = "Playing" ]; then
	url=$(playerctl metadata mpris:artUrl)
	url="i.scdn.co$(sed 's|https://open.spotify.com||g' <<< $url)"
	echo $url
	wget $url -O ~/scripts/currentArt
fi
