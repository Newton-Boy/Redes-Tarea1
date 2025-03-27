#!/usr/bin/python3
# Echo client program
# Version con dos threads: uno lee de stdin hacia el socket y el otro al revés
import jsockets
import sys, threading
import time

def Rdr(s):
    while True:
        try:
            data=s.recv(1500).decode()
        except:
            data = None
        if not data: 
            break
        print(data, end = '')

if len(sys.argv) != 6: # Cambio a 6, porque requerimos size IN y OUT adicionalmente
    print('Use: '+sys.argv[0]+'size IN OUT host port') #sys.argv[0] es el nombre del archivo .py, host=127.0.0.1, y port=?
    sys.exit(1)

s = jsockets.socket_tcp_connect(sys.argv[4], sys.argv[5])
if s is None:
    print('could not open socket')
    sys.exit(1)

# Creo thread que lee desde el socket hacia stdout:
newthread = threading.Thread(target=Rdr, args=(s,))
newthread.start()

# En este otro thread leo desde stdin hacia socket:
for line in sys.stdin:
    s.send(line.encode())

time.sleep(3)  # dar tiempo para que vuelva la respuesta
s.close()

