import socket
from socket_constants import *

print('Recebendo Mensagens...\n\n')

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.bind((HOST_SERVER, SOCKET_PORT))

# Máximo de conexões enfileiradas
tcp_socket.listen(MAX_LISTEN)

while True:
   # Aceita a conexão com o cliente
   conexao, cliente = tcp_socket.accept()
   print('Conectado por: ', cliente)
   while True:
      mensagem = conexao.recv(BUFFER_SIZE)
      if not mensagem: break
      print(cliente, mensagem.decode(CODE_PAGE))
   print('Finalizando Conexão do Cliente ', cliente)
   conexao.close()