import cv2 as cv

img = cv.imread('Images/face_image.jpeg')
cv.imshow('Img',img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average blur',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',gauss)

# Median Blur
median_blur = cv.medianBlur(img,3)
cv.imshow('Median blur',median_blur)

#Bilateral
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral blur',bilateral)

cv.waitKey(0)