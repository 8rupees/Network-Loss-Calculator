import socket

# Server socket setup
server_ip = '127.0.0.1'
server_port = int(input("Enter the port number: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen()

print("Server is waiting for the client to signal readiness...")

# Wait for client's readiness signal
client, address = server.accept()
ready_signal = client.recv(1024).decode()

if ready_signal == "Ready":
    print("Client is ready. Starting data transmission...")

    total_packets = 1000

    for i in range(total_packets):
        message = f"Packet {i}".encode()
        client.send(message)

    print("Data transmission completed.")
else:
    print("Client not ready. Exiting.")

client.close()
server.close()
