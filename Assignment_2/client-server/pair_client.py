#import zeromq library
import zmq

# Get port number of server from user
port=input("Enter Server Port Number which you want to Connect:")

# Creating zmq context object
context=zmq.Context()

# Creating Server Pair Socket
client_socket=context.socket(zmq.PAIR)

# Assigning Server to a ip address and port
client_socket.connect("tcp://127.0.0.1:"+port)

while(True):

    #Response from Server
    message_from_server=client_socket.recv()

    #print message from Server
    print("Server:",message_from_server.decode("utf-8"))

    # take message from user to server
    client_message=input("Type Message which will be send to server:")

    # sending message to server
    client_socket.send_string(client_message)
