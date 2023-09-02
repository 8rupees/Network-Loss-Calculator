import socket

print("""


████████╗░█████╗░██████╗░  ██╗░░░██╗░██████╗  ██╗░░░██╗██████╗░██████╗░
╚══██╔══╝██╔══██╗██╔══██╗  ██║░░░██║██╔════╝  ██║░░░██║██╔══██╗██╔══██╗
░░░██║░░░██║░░╚═╝██████╔╝  ╚██╗░██╔╝╚█████╗░  ██║░░░██║██║░░██║██████╔╝
░░░██║░░░██║░░██╗██╔═══╝░  ░╚████╔╝░░╚═══██╗  ██║░░░██║██║░░██║██╔═══╝░
░░░██║░░░╚█████╔╝██║░░░░░  ░░╚██╔╝░░██████╔╝  ╚██████╔╝██████╔╝██║░░░░░
░░░╚═╝░░░░╚════╝░╚═╝░░░░░  ░░░╚═╝░░░╚═════╝░  ░╚═════╝░╚═════╝░╚═╝░░░░░

█▄▄ █▄█   █▀█ █░█ █▀█ █▀▀ █▀▀ █▀   ▄▀█ █▄░█ █▀▄   █▀█ █▀█ █▀█ █▀█ █ █▀▄
█▄█ ░█░   █▀▄ █▄█ █▀▀ ██▄ ██▄ ▄█   █▀█ █░▀█ █▄▀   █▀▀ █▀▄ █▀▄ █▄█ █ █▄▀
 
          """) # Art Credit to fsymbols.com

def upd():

    sel = None

    while True:
        try:
            print("""Make Your Selection:
            1)Host
            2)Client
                """)
            
            sel = int(input("Enter an input: "))

            if(sel in (1,2)):
                break

            else:
                print("ERROR: MAKE A VALID SELECTION!")

        except:
            print("ERROR: MAKE A VALID SELECTION!")

        finally:
            if(sel == 1):
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

            elif(sel == 2):

                SERVER_IP = '127.0.0.1'
                SERVER_PORT = int(input("Enter the server port number: "))

                client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM = UDP

                total_packets = 1000

                grbg = input("PRESS ENTER AFTER THE SERVER STARTS LISTNING")

                for i in range(total_packets):
                    message = f"Packet {i}".encode()  # Encode the message as bytes
                    client.sendto(message, (SERVER_IP, SERVER_PORT))

                client.close()

            else:
                print("Achievement Unlocked: How Did We Get Here?")


while True:

    print("""

    Select the protocol
          1) TCP
          2) UDP
""")

    try:
        selector = int(input("Select an protocol you want to demonstrate packet loss: "))

        if(selector in (1,2)):
            break

        else:
            print("ERROR: SELECT AND APPROPRIATE OPTION!")
    
    except:
        print("ERROR: SELECT AND APPROPRIATE OPTION!")
    
    finally:

        if(selector == 1):
            pass

        elif(selector == 2):
            upd()

        else:
            print("Achievement Unlocked: How did we get here?")
