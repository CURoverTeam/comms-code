import socket
import sys
 
# Create a connection to the server application on port 81
tcp_socket = socket.create_connection(('localhost', 81))
 
while True:
    data = input("> ")
    if data in ["stop","quit","exit"]:
        print("Closing socket")
        tcp_socket.close()
    tcp_socket.sendall(bytes(data,'utf-8'))