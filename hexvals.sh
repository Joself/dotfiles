#!/bin/bash

# Staggered columns
# i represents the height (amount of rows above and below the center row each).
# j represents the center row width.

if [ $# -eq 0 ]; then
	printf "\x1b[31mCorrect usage:\x1b[0m ./hexvals.sh <min radius>\n"
	exit 1
fi

for ((i=1; i<=$1; i++)); do
	y=$(( 2 * i + 1))
	printf "\x1b[31mCurrent height is $y\x1b[0m\n"
	for ((j=$(($1 + 1)); j>=1; j--)); do
		cur=1
		out=$j
		while [[ $cur -le $i && $j -gt $i ]]; do
			out="$((j-cur)) $out $((j-cur))"
			((cur++))
		done
		if [[ $cur -gt 1 ]]; then
			hex=$(( y * j - i * ( i + 1 ) ))
			printf "$out \x1b[32m$hex\x1b[0m\n"
		fi
	done
done
printf "\n"
