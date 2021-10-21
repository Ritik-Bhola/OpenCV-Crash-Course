import cv2 as cv

img = cv.imread('Images/face_image.jpeg')
cv.imshow("Img",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY) 
cv.imshow("Simple Threshold",thresh)

threshold, thresh_inv = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV) 
cv.imshow("Inverse Simple Threshold",thresh_inv)

# Adeptive Thresholding
adeptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adeptive Threshold",adeptive_thresh)

cv.waitKey(0)