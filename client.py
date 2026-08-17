import socket
import json

# --- Configuration ---
CLIENT_NAME = "Client of Nerf-Em"  # CHANGE THIS to your actual name
SERVER_IP = '127.0.0.1'  # Use '127.0.0.1' for local, or classmate's IP for interop test
SERVER_PORT = 5005       # Must match the server's port (> 5000)

# 1. Accept an integer between 1 and 100 from the keyboard
while True:
    try:
        user_number = int(input(f"Enter an integer (1-100) for {CLIENT_NAME}: "))
        if 1 <= user_number <= 100:
            break  # Valid number, exit the loop
        print("Error: Number must be between 1 and 100. Try again.")
    except ValueError:
        print("Error: Please enter a valid whole number.")

# 2. Open a TCP socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"\nConnecting to server at {SERVER_IP}:{SERVER_PORT}...")
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("[CONNECTED] Successfully connected to server.")

    # 3. Send a message containing your name and the integer
    message_to_send = {
        "name": CLIENT_NAME,
        "number": user_number
    }
    # Convert dictionary to JSON string, then to bytes, then send
    client_socket.sendall(json.dumps(message_to_send).encode('utf-8'))
    print("[SENT] Data sent to server.")

    # 4. Wait for a reply from the server
    print("[WAITING] Waiting for server reply...")
    reply_data = client_socket.recv(1024).decode('utf-8')
    
    # Convert received bytes back to string, then parse JSON
    server_reply = json.loads(reply_data)
    server_name = server_reply.get("name", "Unknown Server")
    server_number = server_reply.get("number", 0)

    # 5. Display the received values and compute their sum
    total_sum = user_number + server_number

    print("\n" + "="*35)
    print("       COMMUNICATION SUMMARY")
    print("="*35)
    print(f"Client's name   : {CLIENT_NAME}")
    print(f"Server's name   : {server_name}")
    print(f"Client's integer: {user_number}")
    print(f"Server's integer: {server_number}")
    print(f"The sum         : {total_sum}")
    print("="*35 + "\n")

except ConnectionRefusedError:
    print("[ERROR] Connection refused! Is the server running?")
except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}")

finally:
    # 6. Terminate after releasing all sockets
    client_socket.close()
    print("[CLOSED] Client socket released. Terminating program.")