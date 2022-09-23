import numpy as np
import cv2
import os

DIR = r'Faces/train'

people = []

for i in os.listdir(DIR):
    people.append(i)

haarCas = cv2.CascadeClassifier('haar_face.xml')
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceRecognizer.read('faceTrain.yml')

img = cv2.imread(r'Faces/val/jerry_seinfeld/httpaurorasblogcomwpcontentuploadsjerryseinfeldpublicityshotjpg.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the face in the image
facesRect = haarCas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x,y,w,h) in facesRect:
    facesRoi = gray[y:y+h,x:x+w]
    
    label, confidence = faceRecognizer.predict(facesRoi)
    print(f'Label = {label} with a confidence of {confidence}')
    
    cv2.putText(img, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=1)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0, 0, 255), thickness=1)

cv2.imshow('Detected Face', img)

cv2.waitKey(0)

