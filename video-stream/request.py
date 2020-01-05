#Used to make get requests to videoStream, while the class is being run from the loop.py script.

import socket
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '0.0.0.0'
port = 1201
server_address = (host, port)

while(True):
    sent = sock.sendto("get".encode('utf-8'), server_address)
    print('sent request')
    time.sleep(1)
