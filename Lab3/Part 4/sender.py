import sys
import socket
import struct

GROUP = sys.argv[1]
PORT = int(sys.argv[2])
SCIPER = sys.argv[3]

msg = SCIPER+input()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.sendto(msg.encode('utf-8'), (GROUP, PORT))

sock.close()
