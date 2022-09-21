import cv2

img = cv2.imread('Photos/birdImgx.jpg')

# BGR to GRAY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# BGR to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  
cv2.imshow('LAB', lab)

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)


cv2.waitKey(0)
