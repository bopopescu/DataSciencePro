import socket


s = socket.socket()


port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
print(s.recv(1024))
print(s.recv(1024))

message=input("Enter message: ")
while message.lower().strip() != 'bye':
    s.send(message.encode())
    data=s.recv(1024).decode()
    print("Message from server",data)
    message=input("Enter text: ")
    # close the connection
s.close()