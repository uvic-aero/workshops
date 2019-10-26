import socket
import cv2
import numpy as np
import sys
import time
import argparse
import base64

HOST = '0.0.0.0'
PORT = 5100
server_socket = (HOST, PORT)

t0 = time.time()
frame_idx = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server_socket)
    while True:
        s.sendall("get".encode('utf-8'))
        data = s.recv(65507)

        array = np.frombuffer(data, dtype=np.dtype('uint8'))
        img = cv2.imdecode(array, 1)
        cv2.imshow("Image", img)

        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
        frame_idx += 1
        # print frame rate
        if frame_idx == 30:
            t1 = time.time()
            sys.stdout.write(
                '\r Framerate : {:.2f} frames/s.     '.format(30 / (t1 - t0)))
            sys.stdout.flush()
            t0 = t1
            frame_idx = 0

cv2.destroyAllWindows()
