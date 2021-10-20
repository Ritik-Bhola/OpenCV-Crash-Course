import cv2 as cv

# img = cv.imread('Images/face_image.jpeg')

# cv.imshow('Img',img)

# Reading videos
vid = cv.VideoCapture('Videos/carsVid.mp4')

while True:
    isTrue, frame = vid.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()

