import numpy as np
import cv2 as cv

def display_lines(frame, lines):
    if lines is not None:
        for line in lines[:100]:
            x1, y1, x2, y2 = line.reshape(4)
            cv.line(img=frame, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=3)
    return frame

# assuming [ B, G, R ]
upper = np.array([ 70, 90, 110])
lower = np.array([ 20, 40, 60 ])

frame = cv.imread('resources/cardboard.jpg')
mask = cv.inRange(frame, lower, upper)
cv.imshow('frame', mask)

# Await until keypress
cv.waitKey(0)
cv.destroyAllWindows()
