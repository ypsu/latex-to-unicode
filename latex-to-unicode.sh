#!/bin/bash

cd "$(dirname $(echo "$0"))"
text=$(./gui.py)
echo -n "$text" | xclip
echo -n "$text" | xclip -selection clipboard
xdotool key shift+Insert
