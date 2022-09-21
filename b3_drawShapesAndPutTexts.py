import cv2
import numpy as np

blank = np.zeros((300,300,3),dtype='uint8')
cv2.imshow('Blank', blank)

# 1. Paint the image a certain colour
blankC = blank
blankC[:] = 0,255,0
cv2.imshow('Green', blankC)

# 2. Paint certain portion
blankD = blank
blankD[200:300, 100:250] = 0,0,255
cv2.imshow('Portion', blankD)

# 3. Draw shape
# to filled the rectangle use -> thickness=cv2.FILLED
cv2.rectangle(blank, (50,0), (100,150), (225,0,0), thickness=2)
cv2.circle(blank, (150,150), 15, (0,100,0), thickness=3)
cv2.line(blank, (50,50), (100,150), (225,225,255), thickness=2)
cv2.imshow('Shape', blank)

# 4. write text
cv2.putText(blank, 'Hello World', (100,120), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,244), thickness=2)
cv2.imshow('Text', blank)

cv2.waitKey(0)