import numpy as np
import cv2 as cv

img = cv.imread("../Images/image.jpg")
cv.imshow("img",img)

cv.waitkey(0)