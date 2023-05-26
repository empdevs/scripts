import socket

def scan(ipAddress, port):
  try:
    print(socket)
    sock = socket.socket()
    print(sock)
    sock.connect((ipAddress, port))
    print(sock)
    serviceVersion = sock.recv(1024)
    print('1',sockVersion)
    serviceVersion = serviceVersion.decode('utf-8')
    print('2',sockVersion)
    serviceVersion = serviceVersion.strip('\n')
    print('3',sockVersion)
    print(f'Port {str(port)} is Open', end=' ')
    print(serviceVersion)
  except ConnectionRefusedError:
    print(f'Port {str(port)} is Closed')
  except UnicodeDecodeErrror:
    print(f'Port {str(port)} is')

target = input('Target: ')
ports = input('Port: ')

if ',' in ports:
    portlist = ports.split(',')
    for port in portlist:
      scan(target, int(port))
elif '-' in ports:
    # portlist = ports.split('-')
    # for port in portlist:
    #   scan(target, int(port))
    portrange = ports.split('-')
    print(portrange)
    start = int(porange[0])
    end = int(porange[1])
    for port in range(start, end):
      target(target, int(port))
else:
  scan(target, int(ports)) 