import socket


def lookup(host):
    return socket.gethostbyaddr(host)[0]
