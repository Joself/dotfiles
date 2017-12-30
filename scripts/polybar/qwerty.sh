#!/bin/bash

if [ -f ~/.config/polybar/qwerty ];
then
	layout="QWERTY"
else
	layout=""
fi

echo "$layout"
