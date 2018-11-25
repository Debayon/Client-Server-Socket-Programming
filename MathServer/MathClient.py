import socket

s = socket.socket()
#host = socket.gethostbyname()
port = 12345

s.connect(('127.0.0.1',port))
print(s.getsockname()[0])
byte = s.recv(1024)
msg = byte.decode()
print(msg)
expression = input()
byte = expression.encode()
s.send(byte)
byte = s.recv(1024)
msg = byte.decode()
print(msg)
s.close()