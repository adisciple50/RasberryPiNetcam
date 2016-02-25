# RasberryPiNetcam
Push Button to capture pic to networked folder.

# Step 1 - Download Script

sudo apt-get install python3-pip

sudo pip3 install opencv

sudo pip3 install picamera

sudo cd ~/Documents/Code/Python

git clone https://github.com/deddokatana/RasberryPiNetcam.git

# Step 2 - Acquire a one button keyboard.

http://www.usbbutton.com/

requires a windows pc to initialy program it.

# Step 3 - Network Drive.

http://theurbanpenguin.com/wp/index.php/setting-up-a-samba-server-on-raspberry-pi/

# Step 4 - Keybindings

install obkey

bind the buttons key combo to the script: "python3 ~/Documents/Code/Python/RasberryPiNetcam/Main.py"

# Step 5 - Sort Out Power

sudo apt-get install xfce4-power-manager

adjust power settings.

# Step 6 - Test The Setup!
 
 check your ~/Pictures folder!
