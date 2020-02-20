import socket
import ssl
import sys

CERT = sys.argv[1]
KEY = sys.argv[2]

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#context.verify_mode = ssl.CERT_REQUIRED
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain(certfile=CERT, keyfile=KEY)

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock = socket.socket()
sock.bind(('127.0.0.1', 5003))

sock.listen(5)
#conn = sock.accept()
# sslsocket = ssl.wrap_socket(
#   conn, server_side=True, certfile=CERT, keyfile=KEY, ssl_version=ssl.PROTOCOL_TLS)
while True:
    sslsocket, fromaddr = sock.accept()

    conn = context.wrap_socket(sslsocket, server_side=True)

    data = conn.read(4096).decode()
    if data:
        print(data)
        conn.send('This is PMU data 0'.encode())
    else:
        break

sslsocket.close()
sock.close()
