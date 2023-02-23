import paramiko
from getpass import getpass
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = '10.0.0.1'
port = 22
user = input('username\n')
pwd = getpass('password\n')

with open('/home/kali/Desktop/lista.txt') as file:
	for user in file:
		print('connecting...')
		ssh.connect(host, port=port, username=user, password=pwd, look_for_keys=False, allow_agent=False)
		print('connected to ' + host)
		shell = ssh.invoke_shell()
		cmd = f'show vpn-sessiondb anyconnect filter name {user}\n'
		shell.send(cmd)
		time.sleep(.5)
		output = shell.recv(65535)
		print(output.decode("utf-8"))
		session = output.decode("utf-8").find('Login Time')
		if session != -1:
			cmd = f'vpn-sessiondb logoff name {user}\n'
			shell.send(cmd)
			output = shell.recv(65535)
			print(output.decode("utf-8"))
		ssh.close()
