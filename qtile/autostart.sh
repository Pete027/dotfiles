#!/bin/sh
echo "Starting nm-applet"

nitrogen --restore &
picom &
dunst &
nm-applet &
sleep 2
volumeicon &
