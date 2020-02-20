from websocket import create_connection
ws = create_connection("ws://tcpip.epfl.ch:5006")
#print("Sending 'Hello, World'...")
msg = "CMD_short:0"
#msg = msg.encode()
ws.send(msg)
print("Sent")
print("Receiving...")
dataset = ''
while True:
    result = ws.recv()
    if(result):
        #       print("Received '%s'" % result)
        dataset += result
    else:
        break
ws.close()

print(dataset)
