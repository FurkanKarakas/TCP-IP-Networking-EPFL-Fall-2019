import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
CMD = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send(CMD.encode('utf-8'))

totaldata = ''

while True:
    data = sock.recv(1024).decode()
    if data:
        totaldata += data
    else:
        break

sock.close()

data = totaldata
totaldata = data.split('T')
totaldata.pop(0)
for i in totaldata:
    print('T'+i)
