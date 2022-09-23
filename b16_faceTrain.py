import cv2
import os
import numpy as np

DIR = r'Faces/train'
haarCas = cv2.CascadeClassifier('haar_face.xml')

# people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# Another way to save folder name...
people = []

for i in os.listdir(DIR):
    people.append(i)

features = []
labels = []
def createTrain():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        
        for img in os.listdir(path):
            imgPath = os.path.join(path,img)
            
            imgArray = cv2.imread(imgPath)
            gray = cv2.cvtColor(imgArray, cv2.COLOR_BGR2GRAY)
            
            facesRect = haarCas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
            
            for (x,y,w,h) in facesRect:
                facesRoi = gray[y:y+h,x:x+w]
                features.append(facesRoi)
                labels.append(label)
                
createTrain()

features = np.array(features, dtype='object')
labels = np.array(labels)

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
faceRecognizer.train(features,labels)

faceRecognizer.save('faceTrain.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

