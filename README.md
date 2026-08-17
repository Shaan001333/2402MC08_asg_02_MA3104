# CN Lab 1 - TCP Socket Programming Assignment

## 📋 Overview
This is a TCP-based client-server application where the client sends its name and a number to the server, and the server responds with its own name and another number. Both client and server display received values and compute their sum.

## 🎯 Objective
Implement a socket programming application that demonstrates:
- TCP connection establishment
- Client-server communication
- Data serialization using JSON
- Interoperability between different clients and servers

## 📋 Requirements

### Client Features
1. Accepts an integer between 1 and 100 from user input
2. Establishes TCP socket connection to server
3. Sends client name and integer to server
4. Receives server's name and integer
5. Displays all values and computes the sum
6. Properly closes all sockets before termination

### Server Features
1. Listens for incoming TCP connections
2. Receives and displays client information
3. Generates a random integer between 1 and 100
4. Sends server name and integer to client
5. Displays all values and computes the sum
6. Terminates if it receives a number outside 1-100 range
7. Properly closes all sockets

## 🛠️ Technical Specifications
- **Protocol**: TCP (Transmission Control Protocol)
- **Port Number**: 5005 (greater than 5000 as required)
- **Data Format**: JSON for interoperability
- **Language**: Python 3.x
- **Socket Type**: SOCK_STREAM

## 📁 Project Structure
