import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

people = ['Billie Eilish']
# features = np.load('../features.npy',allow_pickle=True)
# labels = np.load('../labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('../face_trained.yml')

img = cv.imread(r'/home/rjoker/Projects/OpenCV-Projects/OpenCV-course/Images/Faces/test.jpeg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

# Detect the face in the image
face_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 4)

for (x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img,str(people[label]),(20,20))  
    