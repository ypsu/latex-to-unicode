#!/bin/bash

cd "$(dirname $(echo "$0"))"
./gui.py | tr -d '\n' | xclip
xdotool key shift+Insert
