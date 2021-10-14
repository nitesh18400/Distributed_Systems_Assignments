# THIS IS A PRODUCER. IT ONLY PUSH THE DATA.

import zmq
# LOADING CONTEXT
context = zmq.Context()

# CREATING A PUSH TYPE SOCKET
socket = context.socket(zmq.PUSH)

#ASSIGNING PORT
port = 7000

#BINDING SOCKET TO PORT
socket.bind("tcp://127.0.0.1:{}".format(port))

print("Enter your message. Type exit to quit")

# TAKING MESSAGE INPUT AND SENDING IT IN JSON FORMAT
while(True):
    message = input()
    if(message == "exit"):
        break
    data = {'message':message}
    socket.send_json(data)
