#!/bin/bash
if [ -f ~/.config/polybar/qwerty ];
then
	echo "QWERTY to Dvorak"
	mv ~/.config/polybar/qwerty ~/.config/polybar/dvorak
	setxkbmap -layout se -variant svdvorak
else
	echo "Dvorak to QWERTY"
	mv ~/.config/polybar/dvorak ~/.config/polybar/qwerty
	setxkbmap -layout se
fi

#if [ -f ~/.config/polybar/dvorak ]; then
#	echo "dvorak"
#	mv ~/.config/polybar/dvorak ~/.config/polybar/qwerty
