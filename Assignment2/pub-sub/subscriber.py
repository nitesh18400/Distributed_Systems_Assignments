# IMPORTING LIBRARIES
import zmq
import time
import random
import sys

# LOADING CONTEXT
context = zmq.Context()

# CREATING A SUBSCRIBER TYPE SOCKET
socket = context.socket(zmq.SUB)

# ASSIGNING HOST IP
host = "127.0.0.1"


# MAPPINGS USED FOR FILTERING THE MESSAGES
choice_publisher_mapping = {1:"Computer Science", 
                            2:"Sports", 
                            3:"Entertainment"}

publisher_port_mapping = {"Computer Science": "7000", 
                        "Sports": "8000", 
                        "Entertainment":"9000"}

publisher_topic_mapping = {"Computer Science": ['DSA', 'ML'], 
                        "Sports": ['CRICKET', 'FOOTBALL'], 
                        "Entertainment":['BOLLYWOOD', 'HOLLYWOOD']}


# TAKING SUBSCRIBER PREFERENCES
while(True):
    error = 0
    print("""\nEnter what types of content you want to subscribe to (Comma Seperated like 1,2,3)\n
        1 - Computer Science\n
        2 - Sports\n
        3 - Entertainment\n""")
    choices = []
    choices = list(map(int, input().split(',')))

    for choice in choices:
        if(choice not in choice_publisher_mapping.keys()):
            print("Invalid Choices. Try Again")
            error = 1
            break
    if(error == 0):
        break
    

publishers = []
subscribed = []

# CONNECTING TO ALL THE PUBLISHERS ACCORDING TO THE PREFERENCE
for choice in choices:
    error = 0
    port = publisher_port_mapping[choice_publisher_mapping[choice]]
    try:
        socket.connect ("tcp://localhost:%s" % port)
        print("Successfully Subscribed to ", choice_publisher_mapping[choice])
        subscribed.append(choice_publisher_mapping[choice])
    except:
        print("The publisher ", choice_publisher_mapping[choice], " is not available. You will be subscribed to remaining active publishers based on your choices.\n")
        error = 1

    if(error == 0):
        publishers.append(choice_publisher_mapping[choice])


# COMPILING LIST OF TOPICS THAT ARE SUBSCRIBED
available_topics = []
for sub in subscribed:
    for topic in publisher_topic_mapping[sub]:
        available_topics.append(topic)
        
print("\nBased on your preference following topics are available to subscribe to")
print(available_topics)
print("\nType all the topics you want to subscribe to (Comma Seperated like DSA,BOLLYWOOD)")
subscribed_topics = []
subscribed_topics = list(map(str, input().upper().split(",")))
    
# CREATING FILTER
for topic in subscribed_topics:
    socket.subscribe(topic)

# READING MESSAGES THAT MATCHES THE PREFERENCES
print("\nWaiting for publishers to publish!\n")
for i in range(len(subscribed_topics)*10):
    print(socket.recv_multipart())
    if((i+1)%len(subscribed_topics)==0):
        print("\n")
    

