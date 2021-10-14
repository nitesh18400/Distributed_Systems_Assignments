# IMPORTING LIBRARIES
import zmq
import time
import random
import sys

#LOADING CONTEXT
context = zmq.Context()

#CREATING A PUBLISHER TYPE SOCKET
socket = context.socket(zmq.PUB)

# SETTING HOST IP
host = "127.0.0.1"

# MAPPINGS FOR ASSIGNING PORTS AND SENDING MESSAGES ACCORDING TO TYPE
choice_publisher_mapping = {1:"Computer Science", 
                            2:"Sports", 
                            3:"Entertainment"}

publisher_port_mapping = {"Computer Science": "7000", 
                        "Sports": "8000", 
                        "Entertainment":"9000"}

publisher_topic_mapping = {"Computer Science": ['DSA', 'ML'], 
                        "Sports": ['CRICKET', 'FOOTBALL'], 
                        "Entertainment":['BOLLYWOOD', 'HOLLYWOOD']}

topic_message_mapping = {'DSA':['Heaps are Awesome'], 
                        'ML':['Linear Regression is still most used algo'], 
                        'BOLLYWOOD':['Salman Khan film entered 100 crore market'], 
                        'HOLLYWOOD':['Christopher Nolan best movie'], 
                        'CRICKET':['Virat Kohli hit century'], 
                        'FOOTBALL':['Ronaldo join Manchester United']}


# ASSIGNING TYPE OF PUBLISHER
while(True):
    error = 0
    print("""\nEnter what type of content you want to publish\n
        1 - Computer Science\n
        2 - Sports\n
        3 - Entertainment\n""")
    choice = int(input())
    if(choice not in choice_publisher_mapping.keys()):
        print("Invalid Choice. Try Again")
        error = 1
        
    if(error==0):
        print("Publishing ", choice_publisher_mapping[choice],"\n")
        publisher = choice_publisher_mapping[choice]
        port = publisher_port_mapping[publisher]
        try:
            socket.bind("tcp://*:%s" % port)
        except:
            print("The publisher is already active. Please select others.\n") 
            error = 1
        if(error == 0):
            break   
    
# SENDING MESSAGES ACCORDING TO THE TYPE OF PUBLISHER
while(True):
    topics = publisher_topic_mapping[publisher]
    for topic in topics:
        messages = topic_message_mapping[topic]
        for message in messages:
            socket.send_string(topic, flags=zmq.SNDMORE)
            socket.send_string(message)
            time.sleep(1)
                
socket.clolse()