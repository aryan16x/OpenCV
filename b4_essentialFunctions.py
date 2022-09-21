import cv2

img = cv2.imread('Photos/birdImgx.jpg')

# Converting to grascale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Blurring Image (in some case blurring img removes some noise)
# Here (3,3) is kernal size (must be odd number), to increse blurring effect increse kernal size.
blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

# Edge Cascade
canny = cv2.Canny(img, 125, 175)
# canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny', canny)

# Dilating the image
dilated = cv2.dilate(canny, (3,3), iterations=1)
cv2.imshow('Dilated', dilated)

# Eroding
eroded = cv2.erode(dilated, (3,3), iterations=1)
cv2.imshow('Eroded', eroded)

# Resize
resize = cv2.resize(img, (230,230), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resize', resize)

# Cropping
cropped = img[0:200,12:120]
cv2.imshow('Cropped', cropped)



cv2.waitKey(0)

