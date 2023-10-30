import socket

server = input('\nInforme o nome do HOST ou URL do site: ')

infos = socket.getaddrinfo(host=server, port=80)

print(infos)

for info in infos:
   print('\n----------------------------------------')
   print(f'Info ...................: {info}')
   print(f'Family .................: {info[0]}')
   print(f'Type ...................: {info[1]}')
   print(f'Proto ..................: {info[2]}')
   print(f'Canonical Name (CNAME) .: {info[3]}')   
   print(f'SOCKET Address .........: {info[4]}')