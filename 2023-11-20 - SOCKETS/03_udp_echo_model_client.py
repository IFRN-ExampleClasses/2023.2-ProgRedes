import socket
from socket_constants import *

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem_ida = input('Digite a mensagem (EXIT p/ sair): ')
    mensagem_ida = mensagem_ida.encode(CODE_PAGE)
    udp_socket.sendto(mensagem_ida, (HOST_SERVER, SOCKET_PORT))
    
    if mensagem_ida.decode(CODE_PAGE).upper() == 'EXIT': break

    # Recebendo echo do servidor
    dado_retorno, ip_retorno = udp_socket.recvfrom(BUFFER_SIZE)
    mensagem_volta = data_retorno.decode(CODE_PAGE)
    print (f'Echo recebido {ip_retorno}: {mensagem_volta} ')

# Fechando o socket
udp_socket.close()