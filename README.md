# intrusion_detection_hikey960_demo
Intrusion Detection in a particular region of interest on Hikey960

Intrusion Detection on Hikey-960 allows user to detect motion in a particular region of interest at any remote location. It also sends images back to the user if a motion is detected in that region of interest with the help of mqtt.

Hardware required: Hikey 960, USB Video Camera, PC

Pre-requisites for Hikey960:

sudo apt-get update

sudo apt install python3-dev python3-pip

pip3 install imutils paho-mqtt

OpenCV on python3

Pre-requisites for PC/Laptop:

sudo apt-get update

sudo apt install python3-dev python3-pip

pip3 install paho-mqtt

Perform the following steps for the Intrusion Detection Demo:

Step 1 on PC/Laptop:

Run the mqtt_client_demo.py present in the pc folder

python3 mqtt_client_demo.py

Step 1 on Hikey-960:

Run the trial.py

python3 trial.py

As soon as you run the code the a ROI selector windown will open. Select the Region of interest in which you want to detect any motion with the mouse and press Enter. As any motion is detected in the ROI, it captures the image and sends it back to the user through mqtt.
