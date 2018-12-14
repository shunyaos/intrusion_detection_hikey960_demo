# USAGE
# python motion_detector.py
# python motion_detector.py --video videos/example_01.mp4

# import the necessary packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import sys, os
import base64
s=" "
count = 0
key = 0
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
	vs = VideoStream(src=0).start()
	time.sleep(2.0)

# otherwise, we are reading from a video file
else:
	vs = cv2.VideoCapture(args["video"])

# initialize the first frame in the video stream
firstFrame = None
frame = vs.read()
cv2.imwrite('tp.jpg', frame)
r = cv2.selectROI(frame)
# Crop image
imCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
imCrop = imutils.resize(imCrop, width=500)
trial = cv2.cvtColor(imCrop, cv2.COLOR_BGR2GRAY)
trial = cv2.GaussianBlur(trial, (21, 21), 0)
# Display cropped image
cv2.imshow("Image", imCrop)
cv2.imwrite("image.jpg",imCrop)
cv2.destroyWindow("Image")

# loop over the frames of the video
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	frame = vs.read()
	img = frame
	frame = frame if args.get("video", None) is None else frame[1]
	text = "Unoccupied"
	if(key < 300):
		
		# if the frame could not be grabbed, then we have reached the end
		# of the video
		if frame is None:
			break

		# resize the frame, convert it to grayscale, and blur it
		fCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
		fCrop = imutils.resize(fCrop, width=500)
		gray = cv2.cvtColor(fCrop, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (21, 21), 0)

		# if the first frame is None, initialize it
		if firstFrame is None:
			firstFrame = trial
			continue

		# compute the absolute difference between the current frame and
		# first frame
		frameDelta = cv2.absdiff(firstFrame, gray)
		thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

		# dilate the thresholded image to fill in holes, then find contours
		# on thresholded image
		thresh = cv2.dilate(thresh, None, iterations=2)
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0] if imutils.is_cv2() else cnts[1]

		# loop over the contours
		for c in cnts:
			# if the contour is too small, ignore it
			if cv2.contourArea(c) < args["min_area"]:
				continue

			# compute the bounding box for the contour, draw it on the frame,
			# and update the text
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			text = "Occupied"
		# draw the text and timestamp on the frame
		cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
			(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
		# show the frame and record if the user presses a key
		cv2.imshow("Security Feed", frame)
		#cv2.imshow("Thresh", thresh)
		#cv2.imshow("Frame Delta", frameDelta)
		if text is 'Occupied': 
			count = count + 1
			print(count)
			if count > 50:
				count = count + 1
				print(count)
				cv2.imwrite('intrusion.jpg', frame)
				with open("intrusion.jpg", "rb") as imageFile:
					s=base64.encodestring(imageFile.read())
				#import mqtt_publish_demo
				publish.single("nishant/new", s, hostname="test.mosquitto.org")
				print("Done")
				#os.system("rm -rf intrusion.jpg")
				count = 0
		key = cv2.waitKey(1) & 0xFF
		# if the `q` key is pressed, break from the loop
		if key == ord("q"):
			break


# cleanup the camera and close any open windows
vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()
