import cv2
import numpy as np
import imutils

def display_lines(frame, lines):
    if lines is not None:
        for line in lines[:100]:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(img=frame, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=3)
    return frame

def detect_shape(contour):
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        ar = w / float(h)
        if ar >= 0.95 and ar <= 1.05 and h > 50:
            print('found square')
            return (x, y)
    return -1,-1

frame = cv2.imread('resources/code2.jpeg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
ret, thresh = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY)

contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cont in contours:
    x,y = detect_shape(cont)
    if x > -1: 
        cv2.drawContours(frame, [cont], 0, (0, 255, 0), 2)
        print(x, y)

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
