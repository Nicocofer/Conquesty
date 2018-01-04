#!/usr/bin/python3
# -*- coding: utf-8 -*
import http.server
import threading
import os
import time
from utils.moteur_planete import population
from index import index_conquesty
import dist
import cherrypy

class Authentification(object):
    @cherrypy.tools.sessions()
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="post" action="conquesty">
              Login : <input type="text" value="" name="msg" />
              <button type="submit">Valider</button>
            </form>
          </body>
        </html>"""
    index.exposed = True

    
    @cherrypy.tools.sessions()
    def conquesty(self, msg):
        html = index_conquesty()
        cherrypy.session['user'] = msg
        return html.encode('latin1')
    conquesty.exposed = True
    @cherrypy.tools.sessions()
    def page2(self):
        return cherrypy.session['user'] + "<a href='page1'> Suivant</a>"
    page2.exposed = True
    @cherrypy.tools.sessions()
    def page1(self):
        return cherrypy.session['user'] + "<a href='page2'> Suivant</a>"
    page1.exposed = True
    
def serveur():
    configfile=os.path.join(os.path.dirname(__file__),r"config.conf")
    application = cherrypy.tree.mount(Authentification(), '/')
    cherrypy.quickstart(application, config=configfile)
    
"""    
def serveur():
    PORT = 8888
    server_address = ("", PORT)

    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    handler.cgi_directories = ["/"]
    print("Serveur actif sur le port :", PORT)

    httpd = server(server_address, handler)
    httpd.serve_forever()"""


def moteur_conquesty():
    i=1
    while i<500:
        time.sleep(30)
        
        population()

serveur = threading.Thread(None, serveur)
moteur = threading.Thread(None, moteur_conquesty)
moteur.start() 
serveur.start()
