import socket, sys

#------------------------------------------------------------
def get_protnumber(prefix):
   return dict ((getattr(socket, a), a)
      for a in dir(socket)
         if a.startswith(prefix) )
#------------------------------------------------------------

proto_fam = get_protnumber('AF_')
types     = get_protnumber('SOCK_')
protocols = get_protnumber('IPPROTO_')

server = input('\nInforme o nome do HOST ou URL do site: ')

infos = socket.getaddrinfo(host=server, port='http')

print(infos)

for info in infos:
   family, socktype, proto, canonname, sockaddr = info
   
   print('\n----------------------------------------')
   print(f'Info ...................: {info}')
   print(f'Family .................: {proto_fam[family]}')
   print(f'Type ...................: {types[socktype]}')
   print(f'Proto ..................: {protocols[proto]}')
   print(f'Canonical Name (CNAME) .: {canonname}')   
   print(f'SOCKET Address .........: {sockaddr}')