import socket
import json
import random

# --- Configuration ---
SERVER_NAME = "Server of [Your Name Here]"  # CHANGE THIS to your actual name
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5005       # Port number (must be > 5000)

# 1. Create the main server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This allows the server to reuse the port immediately if it crashes
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"[LISTENING] Server is listening on port {PORT}...")

try:
    # 2. Main loop to keep the server running
    while True:
        # Wait for a client to connect. 
        client_socket, client_address = server_socket.accept()
        print(f"\n[NEW CONNECTION] {client_address} connected.")

        # 3. Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        
        # FIX FOR ERROR 1: Check if the client disconnected without sending data
        if not data:
            print(f"[WARNING] Client disconnected without sending data. Ignoring.")
            client_socket.close()
            continue  # Skip the rest of the loop and wait for the next client

        # Parse the JSON data
        try:
            client_data = json.loads(data)
        except json.JSONDecodeError:
            print(f"[WARNING] Received invalid JSON format. Ignoring.")
            client_socket.close()
            continue

        client_name = client_data.get("name", "Unknown")
        client_number = client_data.get("number", -1)

        # 4. Display the received information
        print(f"Client's name: {client_name}")
        print(f"Server's name: {SERVER_NAME}")
        print(f"Client's integer: {client_number}")

        # 5. THE CRITICAL RULE: Check if the number is between 1 and 100
        if not (1 <= client_number <= 100):
            print(f"[FATAL] Invalid number ({client_number}). Terminating server.")
            client_socket.close() # Close the client connection
            break                 # Break the loop to shut down the server

        # 6. If valid, pick a random number and calculate the sum
        server_number = random.randint(1, 100)
        total_sum = client_number + server_number

        print(f"Server's integer: {server_number}")
        print(f"The sum: {total_sum}\n")

        # 7. Send the response back to the client
        response = {"name": SERVER_NAME, "number": server_number}
        client_socket.sendall(json.dumps(response).encode('utf-8'))

        # 8. Close the connection with this specific client
        client_socket.close()
        print(f"[DISCONNECTED] {client_address} finished.")

except KeyboardInterrupt:
    print("\n[SHUTTING DOWN] Server stopped manually by user.")

finally:
    # 9. ALWAYS close the main server socket when done
    server_socket.close()
    print("[DONE] All server sockets closed. Goodbye!")