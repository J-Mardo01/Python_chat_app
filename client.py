import socket
import threading
from queue import Queue

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            # Receive a message from the server
            message = client_socket.recv(1024).decode()
            # Check if the received message is a termination request from the server
            if message.lower() == "quit":
                print("Server has requested termination. Closing connection...")
                # Close the client socket
                client_socket.close()
                break
            # Print the received message
            print("Received: \n" + message)
        except Exception as e:
            # Print an error message if there is an exception while receiving messages
            print(f"Error receiving message: {e}")
            break

# Function to send messages to the server
def send_message():
    while True:
        # Wait until a message is available in the message queue
        message = message_queue.get()
        try:
            # Send the message to the server
            client_socket.send(message.encode())
            # Print a confirmation message after sending the message
            print("Message sent.")
        except Exception as e:
            # Print an error message if there is an exception while sending messages
            print(f"Error sending message: {e}")
            break

# Function to continuously read user input and add it to the message queue
def input_loop():
    while True:
        # Read user input from the console
        message = input()
        # Add the user input to the message queue
        message_queue.put(message)

if __name__ == "__main__":
    # Create a client socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    # Create a message queue to store messages to be sent to the server
    message_queue = Queue()

    # Create threads for receiving messages, sending messages, and reading user input
    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_message)
    input_thread = threading.Thread(target=input_loop)

    # Start the threads
    receive_thread.start()
    send_thread.start()
    input_thread.start()


