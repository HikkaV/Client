import Client
from Client import Client
from threading import Thread

if __name__ == '__main__':
    host = ''
    port = 8889
    path = '/home/hikkav/environments/my_env/predict/test/1.jpg'
    client = Client(host, port)
    thread_send = Thread(target=client.send_image(path))
    thread_send.start()
