import socket
from Settings import *


class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_image(self, path):

        while True:
            command = str(input())
            while not command in commands:
                print("You tried to use unregistered command."
                      "The list of available commands : "
                      + str(commands))
                command = str(input())

            self.sock.send(bytes(command, "utf8"))
            if not command in commands:
                print(self.sock.recv(4096).decode("utf8"))
            if command == "quit":
                print(self.sock.recv(4096).decode("utf8"))
                break
            with open(path, 'rb') as f:
                mybytes = f.read()
                self.sock.send(mybytes)
            answear = self.sock.recv(4096).decode("utf8")
            if answear == 'GOT IMAGE':
                print('The image was successfully sent')
                self.sock.send(bytes("let's go", "utf8"))
            else:
                continue
            f.close()
            print(self.sock.recv(4096).decode("utf8"))
            prediction = self.sock.recv(4096).decode("utf8")
            print(prediction)
        self.sock.close()
