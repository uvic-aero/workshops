import socket
import cv2
import sys
import argparse
import time
import zlib

jpeg_quality = 50
host = '0.0.0.0'
port = 1201
encoder = 'cv2'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (host, port)

print('Starting up video server on %s port %s\n' % server_address)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 1]
cap = cv2.VideoCapture(0)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4)
    data = data.decode('utf-8')
    if(data == "get"):
        ret, frame = cap.read()
        print("original: ", sys.getsizeof(frame))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (0, 0), fx=0.9, fy=0.9)
        print("after grayscale: ", sys.getsizeof(gray))
        buffer = cv2.imencode('.jpg', gray, encode_param)[1].tostring()
        print("after jpeg: ", sys.getsizeof(buffer))
        buffer = zlib.compress(buffer, 5)
        print("after zlib: ", sys.getsizeof(buffer))
        if buffer is None:
            continue
        if len(buffer) > 65507:
            print("Image too large")
            sock.sendto("FAIL".encode('utf-8'), address)
            continue
        # We send back the buffer to the client
        sock.sendto(buffer, address)
        print('sending')
    elif(data == "quit"):
        keep_running = False
    # time.sleep(0.1)
print("Quitting...")
sock.close()
cap.release()
cv2.destroyAllWindows()
