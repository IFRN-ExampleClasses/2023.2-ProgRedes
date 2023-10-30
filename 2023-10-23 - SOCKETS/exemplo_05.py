import socket, sys

host = input('\nInforme o nome do HOST ou URL do site: ')
port = 22 # Porta HTTP

server_conn = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
   sock.connect(server_conn)
except:
   print(f'\nErro.... {sys.exc_info()}')
else:
   print('\nConexão OK')
   sock.close()