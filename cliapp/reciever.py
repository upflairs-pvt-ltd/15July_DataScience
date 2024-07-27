import socket
# socket.AF_INET   --> THROUGH THE INTERNET 
# socket.SOCK_DGRAM  --> protocol   (UDP/TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ip_address = "192.168.1.65"
ip_address = "127.0.0.1"
port_no = 2525   # 0 - 65353  , 0 to 1023
complete_address = (ip_address,port_no)
s.bind(complete_address) 
print("Hey i am listioning ...")
while True:   # infinite loop 
    Data = s.recvfrom(100)
    message = Data[0]
    message  = message.decode('ascii')
    sender_address = Data[1]
    sender_ip_address = sender_address[0]

    


    print(Message)










