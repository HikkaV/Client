import client
from client import Client
from threading import Thread
from settings import *
if __name__ == '__main__':
    host = host_
    port = port_
    path = path_to_pic
    client = Client(host, port)
    thread_send = Thread(target=client.send_image(path))
    thread_send.start()
