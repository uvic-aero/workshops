import sys
import socket
import time
import signal
import cv2
import numpy as np

# Create socket and listen to port 5100
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("", 5005))
server_socket.listen(5)

cap = cv2.VideoCapture(0)

def signal_handler(signal=None, frame=None):
    exit(0)

while True:
    try:
        client_socket, address = server_socket.accept()
        print("Connected to: ", address)
        cam_url = client_socket.recv(1024)

        ret, frame = cap.read()

        data = cv2.imencode('.jpg', frame).tostring()

    except socket.timeout:
        continue
    except KeyboardInterrupt:
        server_socket.close()
        exit(0)

cap.release()
cv2.destroyAllWindows()
