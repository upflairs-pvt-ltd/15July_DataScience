import socket

# socket.AF_INET   --> THROUGH THE INTERNET 
# socket.SOCK_DGRAM  --> protocol   (UDP/TCP)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

