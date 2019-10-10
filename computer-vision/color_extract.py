import numpy as np
import cv2 as cv

# assuming [ B, G, R ]
upper = np.array([ 70, 90, 110])
lower = np.array([ 20, 40, 60 ])

frame = cv.imread('resources/cardboard.jpg')
mask = cv.inRange(frame, lower, upper)

cv.imshow('frame', mask)

cv.waitKey(0)
cv.destroyAllWindows()
