import cv2 as cv

img = cv.imread('Images/face_image.jpeg')
cv.imshow('Img',img)

# BGR to Grayscle
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L*a*b
Lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('L*a*b',Lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)


cv.waitKey(0)