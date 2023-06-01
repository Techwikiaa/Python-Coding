# first,we need to import the socket modules and then get
# the address and port from the user.
import socket

host = input("Enter the IP address of a server: ")
port = int(input("Enter the server port number: "))

# we create a new socket using the default family socket(AF_INET)
# that uses ipv4 and the default socket type connection-oriented
# TCP-(SOCK_STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)
print("Server started! Waiting for a connections...")
connection, address = s.accept()
print("Client Connected with address:",address)
while True:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'--Message Received-- \n')
    print(data.decode('utf-8'))
connection.close()




