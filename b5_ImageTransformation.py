import cv2
import numpy as np

# Translation
# -x --> left
# -y --> up
# x --> right
# y --> left
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv2.warpAffine(img, transMat, dimension)

# Rotation
# positive angle for anti-clockwise and negative angle for clockwise
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width,height)
    
    return cv2.warpAffine(img, rotMat, dimension)

img = cv2.imread('Photos/birdImgx.jpg')

translated = translate(img, -10, 100)
cv2.imshow('Translated', translated)

rotated = rotate(img, 45)
cv2.imshow('Rotated', rotated)

# Flipping
# here 0 -> vertical flip, 1 -> horizontal flip and -1 -> both flip
flip = cv2.flip(img, 0)
cv2.imshow('Flipped', flip)


cv2.waitKey(0)
