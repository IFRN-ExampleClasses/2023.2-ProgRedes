import socket

host  = input('\nInforme o nome do HOST ou URL do site: ')

ip_host = socket.gethostbyname_ex(host)

print(ip_host)