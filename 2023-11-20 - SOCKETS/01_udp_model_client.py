import socket
from socket_constants import *

# Digitando a mensagem a ser enviada
mensagem = input('Digite a mensagem: ')

# Convertendo a mensagem digitada de string para bytes
mensagem = mensagem.encode(CODE_PAGE)

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviando a mensagem ao servidor      
udp_socket.sendto(mensagem, (HOST_SERVER, SOCKET_PORT))

# Fechando o socket
udp_socket.close()