#!/usr/bin/env python3

import os
import picamera
from subprocess import call
import picamera

# camera = picamera.PiCamera()
output_folder = "/root/Pictures"

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

def takePicture():
    filename = getNextFileName(output_folder) + ".jpg"
    print("Filename: ",filename)
    # os.system("raspistill -t 500 -o " + filename)
    command = "raspistill -o " + filename
    parameter = "-o " + filename
    # call(["raspistill","-o",filename],shell=True)
    call([command],shell=True)

def takePicture2():
    filename = getNextFileName(output_folder) + ".jpg"
    with picamera.PiCamera() as camera:
        camera.resolution = (2592,1944)
        camera.capture(filename)
        camera.close()

def streamcamera():
    call("raspivid -w 640 -h 480 -o - -t 80000 |cvlc --play-and-exit -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264",shell=True)
    

takePicture2()
streamcamera()
