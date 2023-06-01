''' What we are going to write is a program that binds itself
to a specific address and port and will listen for incoming
TCP communcations(a server)
'''

""" 
The following code is a working example of a server. First
we need to import the socket module and the get the address and 
the port form the user
"""
import socket

host = input("Type the server IP address: ")
port = int(input("Type the server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("Server started! waiting for connections...")
connection, address = s.accept()
print('Client connected with address: ',address)
while True:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'--Message Received--\n')
    print(data.decode('utf-8'))
connection.close()
