# RasperiPiDoorbell
A Push Button, On Demand, Intermittent Session Video Streamer

setup instructions:

connect gpio pins 5 and 6 with a pushbutton, or test by shorting the pins to simulate this.

make sure your camera is at /dev/video0 and playable in vlc player


# your rasperi py will only stay on for 30 seconds unless you delete the file from the memory card at /etc/main.py after this step.

## the time that the video transmitted is a global variable - use this to adjust the shutdown time

terminal commands:

cd /etc

sudo wget https://raw.githubusercontent.com/deddokatana/RasperiPiDoorbell/main.py

## verify you are happy with the script - optionally perform sanity checks

terminal commands:

echo "(sleep 5;python scriptname.py)&" >> /etc/rc.local
