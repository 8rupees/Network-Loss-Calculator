import socket

# Client socket setup
server_ip = '127.0.0.1'
server_port = int(input("Enter the port number: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

# Signal readiness to the server
client.send("Ready".encode())

# Wait for server's data transmission
print("Waiting for data from the server...")

total_packets = 1000
received_packets = 0

while received_packets < total_packets:
    message = client.recv(1024).decode()

    if(message == ""):
        received_packets += 1
        pass

    else:
        print(f"\n Received: {message} \n")
        received_packets += 1


print("Data reception completed.")
client.close()

print(f"Packets Received: {received_packets}/{total_packets}")
print(f"Loss Percentage: {float(((total_packets - received_packets) * 100) / 1000)}%" )
