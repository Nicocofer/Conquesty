#!/usr/bin/python3
# -*- coding: utf-8 -*
import http.server
import threading
import os
import time
from utils.moteur_planete import population
from index import index_conquesty
import sqlite3
import cherrypy

class Authentification(object):
    @cherrypy.tools.sessions()
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="post" action="conquesty">
              Login : <input type="text" value="" name="msg" />
              Mot de passe : <input type="password" value="" name="mdp" />
              <button type="submit">Valider</button>
            </form>
          </body>
        </html>"""
    index.exposed = True

    
    @cherrypy.tools.sessions()
    def conquesty(self, msg, mdp):
        cherrypy.session['user'] = ""
        cherrypy.session['mdp'] =  ""       

        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT name,mdp,id FROM Joueur WHERE name='"+str(msg)+"' and mdp='"+str(mdp)+"'")
            for row in cursor:
                cherrypy.session['user'] = row[0]
                cherrypy.session['mdp'] = row[1]
                cherrypy.session['id'] = row[2]
        except:
            pass
        else:
            pass
        
        if cherrypy.session['user'] != "" and cherrypy.session['mdp'] !=  "":
            cursor.execute("SELECT count(*),systeme FROM Planete WHERE id_proprio='"+str(cherrypy.session['id'])+"' GROUP BY systeme ORDER BY count(*) ASC")
            for row in cursor:
                systeme= row[1]
            html = index_conquesty(systeme)
            return html.encode('latin1')
        else:
            return """<html>
              <head></head>
              <body>
              <h1>Login ou mot de passe non valide</h1>
                <form method="post" action="conquesty">
                  Login : <input type="text" value="" name="msg" />
                  Mot de passe : <input type="password" value="" name="mdp" />
                  <button type="submit">Valider</button>
                </form>
              </body>
            </html>"""
    conquesty.exposed = True
    
    
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
