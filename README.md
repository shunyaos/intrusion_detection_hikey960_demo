Intrusion Detection on Hikey960 Demo
=====================================

Intrusion Detection in a particular region of interest on Hikey960

Intrusion Detection on Hikey-960 allows user to detect motion in a particular region of interest at any remote location. It also sends images back to the user if a motion is detected in that region of interest with the help of mqtt.

Hardware required: 
------------------
 * Hikey 960 
 * USB Video Camera
 * PC

Pre-requisites for Hikey960:
----------------------------
  
  * paho-mqtt
  * python3
  * python3-pip
  * imutils
  * OpenCV on python3
  
Except for OpenCV on python3 all the other pre-requisites can be installed by running these commands

```
sudo apt-get update

sudo apt install python3-dev python3-pip

pip3 install imutils paho-mqtt
```

Pre-requisites for PC/Laptop:
-----------------------------
This project has these software pre-requisites to run on PC/Laptop.

  * paho-mqtt
  * python3
  * python3-pip
  
```
sudo apt-get update

sudo apt install python3-dev python3-pip

pip3 install paho-mqtt
```

Steps for the Intrusion Detection Demo:
----------------------------------------
To run a demo of this project please follow these steps.
We assume that you have already installed the pre-requisites before following these steps

Step 1 : Cloning the Project
----------------------------
on PC/Laptop run command to clone this project
```
$ git clone https://github.com/shunyaos/intrusion_detection_hikey960_demo.git
```
on Hikey960 run command to clone this project
```
$ git clone https://github.com/shunyaos/intrusion_detection_hikey960_demo.git
```
Step 2: Starting MQTT on PC/Laptop
----------------------------------
Run the mqtt_client_demo.py present in the pc folder
```
$ cd intrusion_detection_hikey960_demo/pc
$ python3 mqtt_client_demo.py
```
Step 3: Starting the Demo on Hikey960
-------------------------------------
```
$ cd intrusion_detection_hikey960_demo
$ python3 trial.py
```
As soon as you run the code the a ROI selector window will open. Select the Region of interest in which you want to detect any motion with the mouse and press Enter. As any motion is detected in the ROI, it captures the image and sends it back to the user through mqtt.
