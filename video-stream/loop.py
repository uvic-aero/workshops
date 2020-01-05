#Used to test videoStream and connections.

import socket
from videoStream import videoStream

sock = socket.socket()

address = ('0.0.0.0',1201)

vs = videoStream

vs.connections.update(address)
vs.listen()
