import socket
from socket_constants import *

# Criando o socket TDP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

while True:
    mensagem = input('Digite a mensagem: ')

    if mensagem:
        # Convertendo a mensagem digitada de string para bytes
        mensagem = mensagem.encode(CODE_PAGE)
        # Enviando a mensagem ao servidor      
        tcp_socket.send(mensagem)

        # Recebendo echo do servidor
        dado_recebido     = tcp_socket.recv(BUFFER_SIZE)
        mensagem_recebida = dado_recebido.decode(CODE_PAGE)
        print(f'Echo Recebido: {mensagem_recebida}')

# Fechando o socket
tcp_socket.close()