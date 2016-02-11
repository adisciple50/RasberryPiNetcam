# RasperiPiDoorbell
A Push Button, On Demand, Intermittent Session Video Streamer

setup instructions:

make sure your camera is at /dev/video0 and playable in vlc player


# your rasperi py will only stay on for 30 seconds unless you delete the file from the memory card at /etc/main.py after this step.

## the time that the video transmitted is a global variable - use this to adjust the shutdown time


cd /etc

sudo wget https://raw.githubusercontent.com/deddokatana/RasperiPiDoorbell/main.py

## verify you are happy with the script - optionally perform sanity checks

echo "(sleep 5;python scriptname.py)&" >> /etc/rc.local
