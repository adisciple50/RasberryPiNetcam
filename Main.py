import RPi.GPIO as GPIO  # access the gpio button
import time  # deals with time delays
import subprocess  # issues console commands
from SimpleCV import Camera  # captures images
import os  # file operations

# wake from halt
# http://raspberrypi.stackexchange.com/questions/13203/creating-halt-wake-button

# "I have rigged up a wake-from-halt button using pins 5 and 6."
# "These two pins, when connected, will reset power and power on from halt(shutdown)".

#initialise camera
cam = Camera()


## settings
output_folder = "~/Pictures"
streaming_time = 600
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

# capture image
# use simplecv

def capture_image():
    img = cam.getImage()
    return img

# solution for filename auto increment
# http://gis.stackexchange.com/a/27414
def getNextFileName(output_folder):
    highest_num = 0
    for f in os.listdir(output_folder):
        if os.path.isfile(os.path.join(output_folder, f)):
            file_name = os.path.splitext(f)[0]
            try:
                file_num = int(file_name)
                if file_num > highest_num:
                    highest_num = file_num
            except ValueError:
                'The file name "%s" is not an integer. Skipping' % file_name

    output_file_path = os.path.join(output_folder, str(highest_num + 1))
    return output_file_path

def save_image(SimpleCVImage=capture_image()):
    filename = getNextFileName(output_folder)+".png"
    SimpleCVImage.save(filename)

# method found here:
# https://sandilands.info/sgordon/live-webca-streaming-using-vlc-command-line

def start_streaming():
    subprocess.call("vlc -vvv v4l2:///dev/video0 --sout '#transcode{vcodec=mp2v,vb=800,acodec=none}:rtp{sdp=rtsp://:8554/}'",shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stream_for_length_of(duration):
    time.sleep(duration)

def stop_streaming():
    subprocess.call("pkill cvlc",shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def sleep_mode():
    subprocess.call("halt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(.1)


# main function - so run this script on bootup!

save_image()