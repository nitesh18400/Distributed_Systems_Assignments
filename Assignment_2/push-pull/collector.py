# THIS IS A COLLECTOR. IT CAN ONLY PULL THE DATA FROM THE CONSUMERS

# IMPORTING LIBRARIES
import zmq
print("\nCollector has been started all the data will be recieved here...\n")

# LOADING CONTEXT
context = zmq.Context()
pull_port = 8000

# CREATING A PULL TYPE SOCKET
pull_socket = context.socket(zmq.PULL)
pull_socket.bind("tcp://127.0.0.1:{}".format(pull_port))

# DICTIONARIES TO STORE THE INCOMING DATA
messages= {}
ordered_messages=[]

#RECIEVINF DATA FROM CONSUMERS AND STORING ALL THE MESSAGES IN A LIST. ALSO PREPARING CONTRIBUTION DATA SUMMARY.
for i in range(1000):
    data = pull_socket.recv_json()
    carrier = data['Carrier']
    ordered_messages.append(data['data'])
    if(carrier in messages.keys()):
        messages[carrier][0]+=1
        messages[carrier][1].append(data['data'])
    else:
        messages[carrier] = [1,[data['data']]]
    
    # PRINTING DATA SUMMARY FOR EVERY 5 MESSAGES
    if(i%5==0):
        print("\nDATA SUMMARY")
        print("*************")
        print("All messages: ")
        print(ordered_messages)
        print("Contributions: ")
        print(messages)
        
        