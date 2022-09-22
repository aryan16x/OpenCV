import cv2
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rect = cv2.rectangle(blank.copy(), (30,30), (350,350), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

# cv2.imshow('Rect', rect)
# cv2.imshow('Circle', circle)

bitwiseAnd = cv2.bitwise_and(rect, circle)
cv2.imshow('bitwiseAnd',  bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rect, circle)
cv2.imshow('bitwiseOr',  bitwiseOr)

bitwiseXor = cv2.bitwise_xor(rect, circle)
cv2.imshow('bitwiseXor',  bitwiseXor)

bitwiseNot = cv2.bitwise_not(rect)
cv2.imshow('bitwiseNot',  bitwiseNot)


cv2.waitKey(0)
