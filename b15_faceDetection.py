import cv2

img = cv2.imread('Photos/faceImg1.jpeg')
# cv2.imshow('Face img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haarCas = cv2.CascadeClassifier('haar_face.xml')

facesRect = haarCas.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=7)
print(facesRect)

for (x,y,w,h) in facesRect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 1)

cv2.imshow('Detected Face', img)

cv2.waitKey(0)
