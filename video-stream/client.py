import socket
import cv2
import numpy as np
import sys
import time
import argparse
import zlib


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '0.0.0.0'
port = 1201
server_address = (host, port)

# cv2.namedWindow("Image")

t0 = time.time()
frame_idx = 0

while True:
    sent = sock.sendto("get".encode('utf-8'), server_address)
    data, server = sock.recvfrom(65507)
    if (data is not None):
        array = zlib.decompress(data, 0)
        array = np.frombuffer(array, dtype=np.dtype('uint8'))
        final = cv2.imdecode(array, 1)
        cv2.imshow("Image", final)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Asking the server to quit")
            sock.sendto("quit".encode('utf-8'), server_address)
            print("Quitting")
            break
        frame_idx += 1

        if frame_idx == 30:
            t1 = time.time()
            sys.stdout.write(
                '\r Framerate : {:.2f} frames/s.     '.format(30 / (t1 - t0)))
            sys.stdout.flush()
            t0 = t1
            frame_idx = 0

cv2.destroyAllWindows()