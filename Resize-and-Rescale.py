# import cv2 as cv

# img = cv.imread('Images/face_image.jpeg')
# cv.imshow('Img',img)

# def rescaleFrame(frame,scale = 0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)

#     dimensions = (width,height)
    
#     return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow('Resized Image',resized_image)

# cv.waitKey(0)


# Resizing Videos

import cv2 as cv

vid = cv.VideoCapture('Videos/carsVid.mp4')

def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = vid.read()
    cv.imshow('Video', frame)

    frame_resize = rescaleFrame(frame)
    cv.imshow('Resized Video', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
def changeres(width,height):
    # Only work with live video
    vid.set(3,width)
    vid.set(4,height)
vid.release()
cv.destroyAllWindows()

