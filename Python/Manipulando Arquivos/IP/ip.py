import socket
import sys

ips = []
contador = int(input('Insira quantos ips você deseja adicionar: '))              
while len(ips) < contador:         
    ips.append(input('Insira seu ip: '))
for ips_valores in ips:
    addr = ips_valores
    try:
        socket.inet_aton(addr)
        print("IP Valido")
        arq = open('ips.txt', 'a+')
        texto = []
        texto.append(str(ips))
        arq.writelines(texto)
        arq.close()
    except socket.error:
        print("IP Invalido")
        raise 

print('''
    By Guilherme and Lucas W.
''')