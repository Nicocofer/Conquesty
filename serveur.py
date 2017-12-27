#!/usr/bin/python3
# -*- coding: utf-8 -*
import http.server
import threading
import time

def serveur():
    PORT = 8888
    server_address = ("", PORT)

    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    handler.cgi_directories = ["/"]
    print("Serveur actif sur le port :", PORT)

    httpd = server(server_address, handler)
    httpd.serve_forever()


def moteur_conquesty():
    i=1
    while i<500:
        time.sleep(1)
        print(i)
        i=i+1

serveur = threading.Thread(None, serveur)
moteur = threading.Thread(None, moteur_conquesty)
moteur.start() 
serveur.start()
