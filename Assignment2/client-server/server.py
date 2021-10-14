#import zeromq library
import zmq

# zmq object
context=zmq.Context()

# server socket
server_socket=context.socket(zmq.REP)

#Enter Port Number
port=input("Enter the port Number:")

# Assigning Server to a ip address and port
server_socket.bind("tcp://127.0.0.1:"+port)

# starting server
while(True):
    #task from client
    mes=server_socket.recv()

    #print task
    print("Task:",mes.decode("utf-8"))

    #send message to client that message recieved
    server_socket.send_string(port)
