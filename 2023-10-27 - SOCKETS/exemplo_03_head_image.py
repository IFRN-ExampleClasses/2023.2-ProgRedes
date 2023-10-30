import socket

#url_host    = 'www.httpbin.org'
#url_image   = '/image/png'

url_host    = 'ead.ifrn.edu.br'
url_image   = 'portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png'

url_request = f'HEAD /{url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

HOST_PORT   = 443
BUFFER_SIZE = 1024

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, HOST_PORT))
sock_img.sendall(url_request.encode())

print('-'*50)
dados = sock_img.recv(BUFFER_SIZE)
print(str(dados, 'utf-8'))
print('-'*50)

sock_img.close()