Task:
1. To create a multi-threaded Server and client.
2. The client and server will connect over TCP.

3. The client should be able to send a string to the server as many times as it wants.
4. The server will echo the string after appending it with the client's name.
5. The server should be able to connect with multiple clients and communicate with them as in steps 3-4.

Programming language: Java.


#start server Commands

    1. javac Server.java
    2. java Server
    3. Enter Port Number of Server whatever we want
    4. Ctrl+C for closing a server

#Start Client (multiple terminal instances)

    1. javac Clients.java
    2. java Client
    3. Enter Port Number (same as you enteres in server)
    4. Enter Client Name (Uniquely) [It can also be handled using client1,client2, automatically I commented out this part in server.java file]
    5. Start Sending messages to server (from multiple instances of terminal)
    6. Enter quit for closing a client connection


