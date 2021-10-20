import cv2 as cv
import numpy as np 

img = cv.imread('Images/face_image.jpeg')
cv.imshow('Img',img)

# Translate
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(img,100,100)
cv.imshow('Translated', translated)

# Rotate
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None :
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width,height)

    return cv.warpAffine(img,rotMat,dimension)

rotated = rotate(img,30)
cv.imshow("Rotated", rotated)

#Fliping IMG
flipx = cv.flip(img,1)
cv.imshow("Flipx",flipx)

flipy = cv.flip(img,0)
cv.imshow("Flipy",flipy)

flipBoth = cv.flip(img,-1)
cv.imshow("FlipBoth",flipBoth)

cv.waitKey(0)