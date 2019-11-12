# Client side script

# Import all classes from the socket module  
from socket import *
# Create a TCP socket object
s = socket(AF_INET, SOCK_STREAM)

# Setup socket parameters
host = '127.0.0.1'  # IP of the host
port = 7777         # The port number

# Connecting to the server socket
s.connect((host,port))

while True:
    # Sending from client to server, data is encoded with utf-8 charset
    s.send( input('send from client: ').encode('utf-8') )
    
    # Recieving incoming data from the server
    x = s.recv(2048)

    # Print the data after decoding with utf-8 charset
    print('recieved from server: ', x.decode('utf-8'))