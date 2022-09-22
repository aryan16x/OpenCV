import cv2
import numpy as np

img = cv2.imread('Photos/birdImgx.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv2.circle(blank, (img.shape[1]//2,img.shape[0]//2), 50, 255, -1)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Masked', masked)



cv2.waitKey(0)

