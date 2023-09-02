import socket

PORT = int(input("Enter the port number: "))
HOST = '127.0.0.1'

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # DGRAM = UDP

server.bind((HOST, PORT))

total_packets = 1000
recv_packets = 0

grbg = input("PRESS ENTER AFTER THE CLIENT IS READY")

print("Server Is Listening...")

while recv_packets < total_packets:
    try:
        server.settimeout(10.0)  # Set a timeout for recvfrom() (e.g., 10 seconds)
        message, address = server.recvfrom(1024)

        # Decode the received message from bytes to a string
        received_message = message.decode()

        # Compare the received message with the expected format
        expected_message = f"Packet {recv_packets}"

        if received_message == expected_message:
            recv_packets += 1

        print(f"{recv_packets}/{total_packets}")  # Adding extra computational power to simulate real world sinario

    except OSError as e:
        if "timed out" in str(e):
            print("Timeout: No data received within the timeout period...")
            break

print(f"Packets Received: {recv_packets}/{total_packets}")
print(f"Loss Percentage: {float(((total_packets - recv_packets) * 100) / 1000)}%" )

server.close()
