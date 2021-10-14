# THIS IS A CONSUMER. IT PULLS DATA FROM THE PRODUCER AND PUSH IT TO THE COLLECTOR 

# IMPORTING LIBRARIES
import zmq
import random

#LOADING CONTEXT
context = zmq.Context()

# ASSIGNING PORT NUMBERS
pull_port = 7000
push_port = 8000

# CREATING A PULL TYPE SOCKET FOR RECIEVING DATA
pull_socket = context.socket(zmq.PULL)
pull_socket.connect("tcp://127.0.0.1:{}".format(pull_port))

# CREATING A PUSH TYPE SOCKET FOR SENDING DATA
push_socket = context.socket(zmq.PUSH)
push_socket.connect("tcp://127.0.0.1:{}".format(push_port))


# TAKING NAME INPUT FROM THE CONSUMER FOR ID PURPOSE
print("Enter Your Name")
name = input()

id = random.randint(1,10000)
#GENERATING A UNIQUE USERNAME
username = name+str(id)
print("Your assigned username is ",username)
print("\nWorking...\n")

# RECIEVING DATA FROM THE PRODUCER AND SENDING IT TO THE COLLECTOR AFTER ADDING CONSUMER DETAIL
while(True):
    data = pull_socket.recv_json()
    to_pass = "This message is passed via consumer {}".format(id)
    edited_data = {'Carrier': username, 'data':data['message']}
    push_socket.send_json(edited_data)
    print("Data Processed and sent : ",edited_data)
    
    

