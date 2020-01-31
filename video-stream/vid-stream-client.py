import socket
import time
import threading

class Client:
    def __init__(self):
        client1 = threading.Thread(target=self.client)
        client2 = threading.Thread(target=self.client)

        client1.start()
        client2.start()

    def client(self, port=1201):
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host = '127.0.0.1'
        server_address = (host, port)

        while(True):
            sent = sock.sendto("get".encode('utf-8'), server_address)
            print(sent)
            time.sleep(1)

client = Client()

