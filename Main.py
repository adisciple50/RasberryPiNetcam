import RPi.GPIO as GPIO
import time
import subprocess



# wake from halt
# http://raspberrypi.stackexchange.com/questions/13203/creating-halt-wake-button

# "I have rigged up a wake-from-halt button using pins 5 and 6."
# "These two pins, when connected, will reset power and power on from halt(shutdown)".



streaming_time = 30
# in seconds

GPIO.setmode(GPIO.BOARD)
# set pin 5 to input, and enable the internal pull-up resistor
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

oldButtonState1 = True


# function may be redundant, as this script is meant to be run on boot using ("python main.py")

def button_is_pressed():
    buttonState1 = GPIO.input(5)
    if buttonState1 != oldButtonState1 and buttonState1 == False :
        print("Button 1 pressed")
        return True
    else:
        return False

# method found here:
# https://sandilands.info/sgordon/live-webca-streaming-using-vlc-command-line

def start_streaming():
    subprocess.call("cvlc -vvv v4l2:///dev/video0 --sout '#transcode{vcodec=mp2v,vb=800,acodec=none}:rtp{sdp=rtsp://:8554/}'",shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stream_for_length_of(duration):
    time.sleep(duration)

def stop_streaming():
    subprocess.call("pkill cvlc",shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def sleep_mode():
    subprocess.call("halt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(.1)


# main function - so run this script on bootup!

if button_is_pressed():
    start_streaming()
    stream_for_length_of(streaming_time)
    stop_streaming()
    sleep_mode()