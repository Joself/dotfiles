#!/bin/bash

output="—————————"
pos=0

if [[ $? -eq 0 ]]; then
	mpcout="$(mpc -f %name%)"
fi

text=${mpcout%% (*}
text=${text##*   }
songpos=${text%%/*}
songlength=${text##*/}
mpcout=${mpcout##* (}
mpcout=${mpcout%%%)*}

if [ ${#mpcout} -eq 1 ]; then
	pos=0
else
	pos=${mpcout:0:1}
fi

col='\033[0;32m'
nc='\033[0m'

output="%{F#5a5}${output:0:$pos}%{F-}|${output:$pos}"

echo "$songpos $output $songlength"
