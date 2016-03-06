import os
import subprocess

output_folder = "~/Pictures"

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
    call = "raspistill -o %s" % (getNextFileName(output_folder) + ".jpg",)
    print("Calling: ",call)
    subprocess.call(call)

takePicture()