import socket, sys
from socket_constants import *

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o socket a tupla (host, port)
udp_socket.bind((HOST_SERVER, SOCKET_PORT)) 

print(f'\nSERVIDOR ATIVO: {udp_socket.getsockname()}')
print('\nRecebendo Mensagens...\n\n')

try:
    while True:
        mensagem, ip_cliente = udp_socket.recvfrom(BUFFER_SIZE)
        mensagem = mensagem.decode(CODE_PAGE)
        if mensagem.upper() == 'EXIT':
            print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
        else:
            print(f'{ip_cliente}->  {mensagem}')
            # Devolvendo uma mensagem (echo) ao cliente
            mensagem_volta = 'DEVOLVENDO... ' + mensagem
            udp_socket.sendto(mensagem_volta.encode(CODE_PAGE), ip_cliente)
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    udp_socket.close()