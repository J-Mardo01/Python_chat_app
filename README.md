# Overview

I created this project because I wanted to understand on a deeper level how machines communicate to each other. With this project, my goal was to gain practical experience in network programming and multi-threading. 

The networking program I developed is a client-server chat application implemented in Python. The program allows multiple clients to connect to a central server, where they can exchange messages in real-time.

Both the server and the client can be started by running the Python script in the terminal or command prompt. The server will then begin to listen for incoming connections on a specified IP address and port. The server will the display a message indicating it has started and is listening for connections. 

The client will display a welcome message to any users and will allow users to send messages to others in the terminal or command prompt. 

I wrote this software to primarily gain practical experience and deepen my understanding of network programming and concurrent systems. I was able to learn more about using TCP Sockets to establish communication from clients to servers, as well as using concurrent threads to allow multiple users to interact with one another.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Python Chat Application - Youtube Video](https://youtu.be/bMEbp0sx6c8)

# Network Communication

For this project, I decided to use a Client/Server architecture because it allows for easier control, scalability, reliability, and simplicity. 

The server component of the application runs independently and listens for incoming connections from clients. It manages the connections, receives messages from clients, and broadcasts these messages to all other connected clients. The server acts as a central hub for communication.

Multiple clients can connect to the server simultaneously. Each client runs as a separate instance and communicates with the server over the network. Clients can send messages to the server, which then forwards them to all other connected clients. Clients can also receive messages from other clients via the server.

To communicate between client and server I used TCP, which ensures the delivery of the data in the order it was sent. I hard coded the port number 12345, which I learned through research should be an available port.

The messages are text-based messages, which the server identifies who sent the message and broadcasts it to all the clients. 

# Development Environment

For this project I used VS Code as my editing environment and the command line interface in order to send messages to the server and other clients.

I used the Python (3.11.5) programming language to develop this project, and within the python language I used the threading, socket, and queue libraries. 

# Useful Websites

* [Socket Library Documentation](https://docs.python.org/3/library/socket.html)
* [Threading Library Documentation](https://docs.python.org/3/library/threading.html)

# Future Work

* Add funcitonality for user to add name and have it displayed with the message sent.
* Add ability for client to send a private message to another client