#!/bin/bash

if [ -f ~/.config/polybar/dvorak ];
then
	layout="Dvorak"
else
	layout=""
fi

echo "$layout"
