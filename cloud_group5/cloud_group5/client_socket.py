import socket
import sys

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('161.246.70.75', 8023))
clientsocket.send(sys.argv[1])
