#!/bin/bash

if [[ $? -eq 0 ]]; then
	length="$(mpc -f %name%)"
fi

length=${length%% (*}
length=${length##*   }
length=${length##*/}

echo "$length"
