import socket, threading

SERVER = '0.0.0.0'
PORT = 5678

def cliInteraction(sockConn, addr):
    msg = b''
    while msg != b'!q':
        try:
            msg = sockConn.recv(512)
            broadCast (msg, addr)
        except:
            msg = b'!q'
    allSocks.remove ((sockConn, addr))
    sockConn.close()

def broadCast(msg, addrSource):
    msg = f"{addrSource} -> {msg.decode('utf-8')}"
    print (msg)
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))

try:
    allSocks = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER, PORT))

    print ("Listening in: ", (SERVER, PORT))
    sock.listen(5)

    while True:
        sockConn, addr = sock.accept()
        print ("Connection from: ", addr)
        allSocks.append((sockConn, addr))
        tClient = threading.Thread(target=cliInteraction, args=(sockConn, addr))
        tClient.start()
except Exception as e:
    print ("Fail: ", e)
