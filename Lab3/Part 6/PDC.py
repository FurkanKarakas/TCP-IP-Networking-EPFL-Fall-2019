from websocket import create_connection
import sys

SV = sys.argv[1]
PORT = sys.argv[2]
CMD = sys.argv[3]

STR = """ws://"""+SV+':'+PORT
sock = create_connection(STR)
sock.send(CMD)
i = 0

while True:
    i += 1
    data = sock.recv()
    if data:
        print(data.decode())
    else:
        break

print(i)
sock.close()
