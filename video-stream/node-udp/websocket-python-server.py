import socket
import cv2
import sys
import argparse
import time
import base64


def get_frame_buffer(cap):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (0, 0), fx=0.1, fy=0.1)
    img = cv2.imencode('.jpg', gray)[1]
    # return img.tostring()
    return base64.b64encode(img)


jpeg_quality = 50
HOST = ''
PORT = 5100
encoder = 'cv2'

cap = cv2.VideoCapture(0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Listening on %s port %s\n' % (HOST, PORT))
    conn, addr = s.accept()
    print('Connected by', addr)

    while True:
        data = conn.recv(4)
        data = data.decode('utf-8')
        if(data == "get"):
            buffer = get_frame_buffer(cap)
            if len(buffer) > 65507:
                print("Image too large")
                continue
            print("img size: ", sys.getsizeof(buffer))
            if buffer is None:
                print("buffer is None")
                continue
            conn.sendall(buffer)
            time.sleep(2.0)
