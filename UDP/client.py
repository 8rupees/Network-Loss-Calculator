import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = int(input("Enter the server port number: "))

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM = UDP

total_packets = 1000

grbg = input("PRESS ENTER AFTER THE SERVER STARTS LISTNING")

for i in range(total_packets):
    message = f"Packet {i}".encode()  # Encode the message as bytes
    client.sendto(message, (SERVER_IP, SERVER_PORT))

client.close()