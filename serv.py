import socket
import sys
import os
import _thread
import time

ip = input(' - Digite o endereço IP a conectar: ')
if ip == '':
 print(' [!] Nenhum IP informado. Padrão: 127.0.0.1\n')
 ip = '127.0.0.1'

port = input(' - Digite a porta a conectar: ')
if port == '':
 print(' [!] Nenhuma porta informada. Padrão: 1234\n')
 port = 1234
n = input(' - Digite o seu nome nesta conversa: ')
if n == '':
 n = 'Sem nome'
print('\n Ok '+n+'. Aguarde uma conexão ser estabelecida...')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, int(port)))
s.listen(2)

con, addr = s.accept()
print('\n ==> Conectado com ',addr,'. Sucesso!')
print('''   ___  _           _                     
  / __|| |_   __ _ | |_     _ __  _  _ 
 | (__ | ' \ / _` ||  _| _ | '_ \| || |
  \___||_||_|\__,_| \__|(_)| .__/ \_, |
                           |_|    |__/ 
 [*] Bem vindo ao chat.py!
''')

def enviarmsg():
 while True:
  msg = input('\nEu > ')
  con.send(msg.encode('utf-8'))
def recmsg(tn, delay):
 while True:
  r = con.recv(1024)
  rec = r.decode('utf-8')
  print('\n')
  print(rec + '\n\nEu > ',end='')
while True:
 _thread.start_new_thread(recmsg, ('Thread-1', 1))
 enviarmsg()
con.close()


