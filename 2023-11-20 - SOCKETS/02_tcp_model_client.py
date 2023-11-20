import socket
from socket_constants import *

# Digitando a mensagem a ser enviada
mensagem = input('Digite a mensagem: ')

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

# Convertendo a mensagem digitada de string para bytes
mensagem = mensagem.encode(CODE_PAGE)

# Enviando a mensagem ao servidor      
tcp_socket.send(mensagem)

# Fechando o socket
tcp_socket.close()