import cv2
import numpy as np
from matplotlib import pyplot as plt
import ctypes

cap = cv2.VideoCapture(1)

while(1):
	_,frame = cap.read()
	
	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_,thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
	
	# Erosion + dilation = opening
	kernel = np.ones((5,5),np.uint8)
	opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
	
	# Finding contours
	img, contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE )
	
	# Draw contours
	cv2.drawContours(opening, contours, -1,(0, 255,0), 6)
	
	# Calculating area under contours
	cnt = contours[0]
	area = cv2.contourArea(cnt)
	print(area)
	
	cv2.imshow('frame',frame)
	#cv2.imshow('gay image',gray_img)
	cv2.imshow('binary',thresh)
	cv2.imshow('opening',opening)
	
	# Show "PEEP PEEP"
	if area < 200  :
		print("PEEP PEEP! Give side to the car at the back.")
		ctypes.windll.user32.MessageBoxW(0,"Give side to the car at the back.","PEEP PEEP!", 1)
		
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()