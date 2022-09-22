import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('Photos/birdImgx.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blank = np.zeros(gray.shape[:2], dtype='uint8')
mask = cv2.circle(blank, (gray.shape[1]//2,gray.shape[0]//2), 50, 255, -1)
masked = cv2.bitwise_and(gray, gray, mask=mask)
cv2.imshow('Masked', masked)

# Grayscale Histogram
grayHist = cv2.calcHist([gray], [0], masked, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('num of pixels')
plt.plot(grayHist)
plt.xlim([0,256])
plt.show()

# Color Histogram
mask = cv2.circle(blank, (img.shape[1]//2,img.shape[0]//2), 50, 255, -1)
masked = cv2.bitwise_and(img, img, mask=mask)

colour = ('b', 'g', 'r')
for i,col in enumerate(colour):
    hist = cv2.calcHist([img], [i], mask, [255], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,255])

plt.show()

cv2.waitKey(0)
