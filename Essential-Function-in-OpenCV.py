import cv2 as cv

img = cv.imread('Images/face_image.jpeg')
cv.imshow('Img',img)

# Conveting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

# Edge Cascade
canny = cv.Canny(img,125,175)
cv.imshow("Canny",canny)

#Dilation the image
dilate = cv.dilate(canny, (3,3),iterations=1)
cv.imshow("Dilated Img", dilate)

#Eroding
erode = cv.erode(dilate, (3,3),iterations=1)
cv.imshow("Eroded Img", erode)

#Resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized Img",resized)

#Cropping
cropped = img[50:100, 100:150]
cv.imshow("Cropped img",cropped)

cv.waitKey(0)