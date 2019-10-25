import socket
import cv2
import sys
import argparse
import time
import base64

jpeg_quality = 50
host = ''
port = 5100
encoder = 'cv2'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (host, port)

print('starting up on %s port %s\n' % server_address)

cap = cv2.VideoCapture(0)

sock.bind(server_address)
data, address = sock.recvfrom(100)
print(address)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (0, 0), fx=0.1, fy=0.1)
    img = cv2.imencode('.jpg', gray)[1]
    buffer = base64.b64encode(img)
    print(buffer)
    print("img size: ", sys.getsizeof(buffer))
    if buffer is None:
        print("buffer is None")
        continue
    # We send back the buffer to the client
    print("Sending")
    sock.sendto(buffer, address)
    print("sent")
    time.sleep(2.0)

print("Quitting..")
sock.close()
