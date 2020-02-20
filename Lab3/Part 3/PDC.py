import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
CMD = 'RESET:20'

sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

sock4.settimeout(1)
sock6.settimeout(1)
counter = 0

sock4.connect((HOST, PORT))
sock6.connect((HOST, PORT))

while True:
    counter += 1
    sock4.send(CMD.encode('utf-8'))
    sock6.send(CMD.encode('utf-8'))
    data4 = ''
    data6 = ''
    try:
        data4 = sock4.recv(1024).decode()
    except:
        pass

    try:
        data6 = sock6.recv(1024).decode()
    except:
        pass

    if data4:
        print(data4)
        print(counter)
        break
    elif data6:
        print(data6)
        print(counter)
        break

sock4.close()
sock6.close()
