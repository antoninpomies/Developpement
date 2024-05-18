#!/usr/bin/python3
import socket, re # import socket obligatoire, re pour les expressions regulières

readresseip = re.compile(rb'"ip": "[0-9]\.+"') # on rajoute rb pour Raw et Byte

ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur = ('ipinfo.io', 80) # port 80 correspondant à http

ma_socket.connect(serveur)
ma_socket.sendall(b'GET/HTTP/1.0\r\n\r\nHost:ipinfo.io\r\n\r\n')
while 1:
    ligne = ma_socket.recv(1024)
    if not ligne:
        break
    resultat = readresseip.search(ligne)
    if resultat:
        print(resultat.group(1))
ma_socket.close()