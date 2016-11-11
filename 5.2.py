#
# Simple web server for assignment Week 2
#
#

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind(('', 1234))
except socket.error:
    print("Bind failed")
    sys.exit()

s.listen(5)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    print('Got a request!')

conn.close()
s.close()
