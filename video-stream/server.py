import socket
import cv2
import sys
import argparse
import time

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

while True:
    data, address = sock.recvfrom(4)
    data = data.decode('utf-8')
    if(data == "get"):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (0, 0), fx=0.1, fy=0.1)
        buffer = cv2.imencode('.jpg', gray)[1].tostring()
        print("img size: ", sys.getsizeof(buffer))
        if buffer is None:
            continue
        if len(buffer) > 65507:
            print("Image too large")
            sock.sendto("FAIL".encode('utf-8'), address)
            continue
        # We send back the buffer to the client
        sock.sendto(buffer, address)
    elif(data == "quit"):
        grabber.stop()
        keep_running = False
    time.sleep(0.1)
print("Quitting..")
grabber.join()
sock.close()
