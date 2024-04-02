import socket
import threading

# Variable to keep the server runnning
server_running = True

# Function to handle client communication
def handle_client(client_socket, address):
    while server_running:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode()
            if not message:
                print(f"Client {address} disconnected")
                # close client socket and remove client from list of clients
                client_socket.close()
                clients.remove(client_socket)
                break
            #print received message and sender of message
            print(f"Received message from {address}: {message}")
            #print("I AM HERE!!!!!!!!!!!")      debugging statement
            # Broadcast the received message to all clients
            broadcast(message, client_socket)
            #print("NOW I AM HERE!!!!!!!")      debugging statement
        except Exception as e:
            # Print error message if an exception occurs 
            print(f"Error handling client {address}: {e}")
            client_socket.close()
            clients.remove(client_socket)
            break

# Function for broadcasting messages
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                # Send message to client(s)
                #print("I AM HERE IN BROADCAST")    debugging
                client.send(message.encode())
                #print("NOW I AM HERE IN BROADCAST")    debugging
            except Exception as e:
                print(f"Error broadcasting message to a client: {e}")
                # close client socket and remove client from list of clients
                client.close()
                clients.remove(client)

# Terminates server gracefully
def stop_server():
    global server_running
    server_running = False
    # Close all client sockets
    for client_socket in clients:
        client_socket.close()
    # Join all client handler threads
    for client_handler in client_handlers:
        client_handler.join()
    # Close the server socket
    server.close()

# Sends welcome message
def welcome_message(client_socket):
    welcome_message = "Welcome to the chat. Type QUIT to close your connection."
    client_socket.send(welcome_message.encode())

if __name__ == "__main__":
    # Create server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)

    clients = []
    client_handlers = []

    print("Server started. Listening for connections...")

    try:
        # Main loop to accept imcoming client connections
        while True:
            # Accept client
            client_socket, client_address = server.accept()
            print(f"Client {client_address} connected")
            clients.append(client_socket)
            welcome_message(client_socket)
            # Start client handler thread
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            # Add thread to list of client handlers
            client_handler.start()
    # Allows Ctrl+C to stop server
    except KeyboardInterrupt:
        print("Server stopping...")
        stop_server()
        print("Server Stopped")
