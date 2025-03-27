#!/usr/bin/python3
# Echo server program - version of server_echo4_n.c
# Usando threads para multi-clientes
import os, signal
import sys, threading
import jsockets

class ClientThread(threading.Thread):
    def __init__(self, addr, s):
        threading.Thread.__init__(self)
        self.sock = s
    def run(self):
        print('Cliente Conectado')
 
        while True: # Escucho hasta que no me hablen más
            data = self.sock.recv(1024*1024)
            if not data: break
            self.sock.send(data) # Retorno la el mismo dato que me pasaron
        self.sock.close()
        print('Cliente desconectado')

# Main
s = jsockets.socket_tcp_bind(1818)
if s is None:
    print('could not open socket')
    sys.exit(1)
while True:
    conn, addr = s.accept()  # Espero a conectar con un cliente, acción bloqueante
    newthread = ClientThread(addr, conn) # Creo Thread que inicializará ClientThread
    newthread.start()
