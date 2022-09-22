import cv2

img = cv2.imread('Photos/birdImgx.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Simple thresholding
# if val>150 then it set to be 255 (we can also set different value)
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholded', thresh)

threshold, threshInv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Thresholded inv', threshInv)

# Adaptive thresholding
# adaptive = cv2.adaptiveThreshold(gray, 150, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 3)
adaptive = cv2.adaptiveThreshold(gray, 150, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 3)
cv2.imshow('Adaptive thresholding',adaptive)


cv2.waitKey(0)
