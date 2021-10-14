import zmq

server_numbers=int(input("enter number of servers which you want to connect:"))

# zmq object
context=zmq.Context()

#get port Numbers of servers from users
ports=list(map(str,input("Enter the port Number of the server which you want to connect:").split()))

# Creating Server Req Socket
client_socket=context.socket(zmq.REQ)

# Connecting Clients to all server
for port in ports:
    client_socket.connect("tcp://127.0.0.1:"+str(port))

#number of tasks that client send to servers in distributed manner
task=int(input("Enter number of request for server:"))

#Sending task
for request in range(task):
    #task request
    client_socket.send_string("task"+str(request))
    #message from client
    server_mes=client_socket.recv()
    if(server_mes.decode("utf-8") in ports):
        print("server:"+"Task "+ str(request)+" Done by Server",ports.index(server_mes.decode("utf-8")))

    #print message from server
    
