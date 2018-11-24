import socket

s = socket.socket()
#host = socket.gethostbyname()
port = 12345

s.connect(('127.0.0.1',port))
print(s.getsockname()[0])
byte = s.recv(1024)
msg = byte.decode()
print(msg)
print("Please enter the first letter of the item you want to buy followed by the quantity")
msg = input()
byte = msg.encode()
s.send(byte)
input()
s.close()