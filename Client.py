import sys
import socket
import signal
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def signal_handler(signal, frame):
  global sock

  print('\nExiting')
  sock.close()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

cnt = 0

while(1):
  #Send a message to the server
  message = 'This is messsage #' + str(cnt)
  cnt += 1
  time.sleep(1)
  sock.sendall(message)
  sent_bytes = len(message)

  #Receive and print messages from the server
  recv_bytes = 0
  data = ''
  while recv_bytes < sent_bytes:
    data += sock.recv(sent_bytes)
    recv_bytes += len(data)

  print >>sys.stderr, '(CLIENT): received "%s"' % data 
    
