import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	
	redimage = frame[:,:,2]
	redglobmean = np.mean(redimage)
	
	greenimage = frame[:,:,1]
	greenglobmean = np.mean(greenimage)
	
	blueimage = frame[:,:,0]
	blueglobmean = np.mean(blueimage)
	
	color_detect = [blueglobmean, greenglobmean, redglobmean]
	print (color_detect)
	
	k = cv2.waitKey(1000) & 0xFF
	if k == ESC:
		break
