import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")
c, addr = s.accept()
print('Got connection from', addr)
c.send(b'Thank you for connecting')
c.send(b'U r now connected to server how may i hepl u')

while True:

    data = c.recv(1024).decode()
    if not data:
        # if data is not received break
        break
    print("from connected user: " + str(data))
    data = input('Enter Text:  ')
    c.send(data.encode())  # send data to the client

c.close()