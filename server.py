# Server side script

# Import all classes from the socket module  
from socket import *
# Create a TCP socket object
s = socket(AF_INET, SOCK_STREAM)

# Setup socket parameters
host = '127.0.0.1'  # IP of the host
port = 7777         # The port number

# Binding the socket to the script
s.bind((host,port))

# Listening for Incoming Connections, maximum of 5
s.listen(5)

# Accept incoming connections from clients
c,a = s.accept() # c: The socket object of the client, a: Client info (IP, port)

# Printing the client info
print("Connected with client \n", a)

while True:
    # Recieving incoming data from a client
    x = c.recv(2048)

    # Print the data after decoding with utf-8 charset
    print('recieved from client: ', x.decode('utf-8'))

    # Sending from server to client, data is encoded with utf-8 charset
    c.send( input('send from server: ').encode('utf-8') )
