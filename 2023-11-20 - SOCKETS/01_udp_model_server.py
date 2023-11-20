import socket, sys
from socket_constants import *

print('Recebendo Mensagens...\n\n')

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ligando o socket a porta
udp_socket.bind(('', SOCKET_PORT))

try:
    while True:
        # Recebendo os dados do cliente
        mensagem, ip_cliente = udp_socket.recvfrom(BUFFER_SIZE)
        print(f'O cliente {ip_cliente} enviou: {mensagem.decode(CODE_PAGE)}')
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    udp_socket.close()