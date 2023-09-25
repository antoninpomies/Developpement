#Faire le debug du programme suivant et expliquer ce qu'il fait
import socket, re

re_address_ip = re.compile(r'"ip": "[0-9\.]+"')

ma_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tsap_serveur = ("ipinfo.io", 80)

ma_socket.connect(tsap_serveur)
ma_socket.sendall(b"GET / HTTP/1.0\r\nHost: ipinfo.io\r\n\r\n")
while 1:
    print(ma_socket.recv(1024))
    if not ma_socket.recv(1024):
        print(resultat.group(1))
ma_socket.close()
