import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# target_ip = "192.168.1.65"
target_ip = "127.0.0.1"  # localhost 
target_port =  2525
target_address = (target_ip,target_port)
condition = True
while condition:
    message = input("plz enter your message : ")
    message_encrypted = message.encode('ascii')
    s.sendto(message_encrypted,target_address)
    print("Your message is sent .....")
    permission = input("")

    if permission == "Y" or permission == "y":
        condition = False 






