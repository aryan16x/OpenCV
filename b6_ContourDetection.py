import cv2
import numpy as np

# Contour is usefull tool for shape analysis, object detection and recognition

img = cv2.imread('Photos/birdImgx.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
canny = cv2.Canny(blur, 125, 175)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# there is aldo different types of RETR and diffrent types of CHAIN_APPROX, so you can check it on google.
# Here, LIST will return all posible contours.
print(len(contours));

# Another method
ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresh Image', thresh)
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours));

contoursD = cv2.drawContours(img, contours, -1, (0,0,255), 2)
cv2.imshow('Contours', contoursD)


cv2.waitKey(0)
