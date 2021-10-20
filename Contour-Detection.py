import cv2 as cv
import numpy as np

img = cv.imread('Images/face_image.jpeg')
cv.imshow('Img',img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Drawn Contours', blank)

cv.waitKey(0)