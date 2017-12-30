#!/bin/bash

if [[ "$(playerctl -l)" = *"spotify"* ]] &>/dev/null; then
	playerctl metadata title
fi
