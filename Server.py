import sys
import socket
import signal

connected = False

def signal_handler(signal, frame):
  global connection
  global connected

  print('\nExiting')
  if (connected):
    connection.close()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

connected = True
print >>sys.stderr, 'connected'

print >>sys.stderr, 'connection from', client_address

while connected:
  # Receive the data in small chunks and retransmit it
  data = connection.recv(1024)
  if data:
    print >>sys.stderr, '(SERVER): received "%s"' % data
    connection.sendall(data)
