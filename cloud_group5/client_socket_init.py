import socket
import sys
from time import sleep

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('161.246.70.75', 8025))
clientsocket.send(sys.argv[1])