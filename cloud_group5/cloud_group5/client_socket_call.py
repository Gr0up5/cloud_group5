import socket
import sys
from time import sleep

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('161.246.70.75', 8024))
clientsocket.send(sys.argv[1])

while True:
	reply = clientsocket.recv(131072)

	if reply == '0':
		# success
		sys.exit(0)

	else:
		# fail
		sys.exit(1)
