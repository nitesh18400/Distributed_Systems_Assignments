#import zeromq library
import zmq

# Get port number from user
port=input("Enter Port Number on which you want to host Server:")

# Creating zmq context object
context=zmq.Context()

# Creating Server Pair Socket
server_socket=context.socket(zmq.PAIR)

# Assigning Server to a ip address and port
server_socket.bind("tcp://127.0.0.1:"+port)

connection_status=True

# starting server
while(True):
    #First time Connection Response
    if(connection_status):
        server_socket.send_string("Client Connected")
        print("Client Connected")
        connection_status=False
    # message recieved
    else:
        server_socket.send_string("Recieved Your Message")
    
    #message from client
    msg_from_client=server_socket.recv()

    #printing client message
    print("Client:",msg_from_client.decode("utf-8"))
