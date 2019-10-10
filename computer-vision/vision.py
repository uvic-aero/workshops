import cv2
import numpy as np

def display_lines(frame, lines):
    line_image = np.zeros_like(frame)
    if lines is not None:
        for line in lines[:100]:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(img=line_image, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=3)
    return line_image

lower_brown = np.array([])
upper_brown = np.array([])

frame = cv2.imread('resources/cardboard.jpg')
blur = cv2.GaussianBlur(frame, (5,5), 0)
canny = cv2.Canny(blur, 50, 150)
print(frame[0])
lines = cv2.HoughLinesP(canny, 2, np.pi/180, 100, np.array([]), minLineLength=50, maxLineGap=20)

frame_with_lines = display_lines(frame, lines)

cv2.imshow('frame',frame_with_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
