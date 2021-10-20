import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Black", blank)

# 1. Point the image a certiain color
blank[:] = 0,255,0
cv.imshow("Green",blank)

blank[200:300,300:400] = 0,0,255
cv.imshow("Green croped",blank)

# 2. Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2) # if we set thickness = -1 then the rectange will be filled
cv.imshow("Rectangle",blank)

# 3. Draw a circle 
cv.circle(blank,(250,250),40,(255,0,0),thickness=2) # if we set thickness = -1 then the rectange will be filled
cv.imshow("Circle",blank)

# 4. Draw a line 
cv.line(blank,(0,0),(250,250),(0,0,255),thickness=2)
cv.imshow("Line",blank)

# 5. Write Text
cv.putText(blank,"Hello",(300,300),cv.FONT_HERSHEY_TRIPLEX,1.0,(100,200,130),2)
cv.imshow("Text",blank)

cv.waitKey(0)
