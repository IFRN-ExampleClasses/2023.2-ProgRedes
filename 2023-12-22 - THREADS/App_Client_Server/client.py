import socket, threading

SERVER = 'localhost'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '

def servInteraction():
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(512)
            print ("\n"+msg.decode('utf-8')+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '!q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode('utf-8'))
        except:
            msg = '!q'
    closeSocket()

def closeSocket():
    try:
        sock.close()
    except:
        None

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))

    print ("Conectado a: ", (SERVER, PORT))
    tServer = threading.Thread(target=servInteraction)
    tUser = threading.Thread(target=userInteraction)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
except Exception as e:
    print ("Falha ", e)

