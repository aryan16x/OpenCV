import cv2

img = cv2.imread('Photos/birdImgx.jpg')

# 1. Averaging
avg = cv2.blur(img, (3,3))
cv2.imshow('Avg', avg)

# 2. Gaussian blur
# Here sigmaX is for std deviation in x direction
gb = cv2.GaussianBlur(img, (3,3), sigmaX=0)
cv2.imshow('GaussianBlur', gb)

# 3. Median blur
# This is more effective to reduce noise
mb = cv2.medianBlur(img, 3)
cv2.imshow('MedianBlur', mb)

# 4. Bilateral blur
bb = cv2.bilateralFilter(img, 5, 25, 21)
cv2.imshow('Bilateral blur', bb)


cv2.waitKey(0)
