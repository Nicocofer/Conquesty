#!/usr/bin/python3
# -*- coding: utf-8 -*
import http.server
import threading
import os
import time
from utils.moteur_planete import population, max_pop, hangar_metal, metal, hangar_gaz, hangar_cristal, cristal, gaz, energie
from index import index_conquesty
import sqlite3
import cherrypy

class Authentification(object):
    @cherrypy.tools.sessions()
    def index(self):
        cherrypy.session['user'] = ""
        cherrypy.session['mdp'] = ""
        cherrypy.session['id'] = ""
        return """<html>
          <head><link rel="stylesheet" type="text/css" href="/dist/css/login.css"></head>
          <body>
            <h1>Conquesty</h1>
            <form method="post" action="log">
              Login : <input type="text" value="" name="msg" />
              Mot de passe : <input type="password" value="" name="mdp" />
              <button type="submit">Valider</button>
              <a href="inscription">Insciption</a>
            </form>
          </body>
        </html>"""
    index.exposed = True

    @cherrypy.tools.sessions()
    def log(self, msg, mdp):
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
            return self.conquesty()
        else:
            return """<html>
              <head><link rel="stylesheet" type="text/css" href="/dist/css/login.css"></head>
              <body>
              <p>Login ou mot de passe non valide</p>
               <h1>Conquesty</h1>
                <form method="post" action="log">
                  Login : <input type="text" value="" name="msg" />
                  Mot de passe : <input type="password" value="" name="mdp" />
                  <button type="submit">Valider</button>
                  <a href="inscription">Insciption</a>
                </form>
              </body>
            </html>"""
    log.exposed = True
    
    @cherrypy.tools.sessions()
    def conquesty(self):
            conn = sqlite3.connect('Base_conquesty.db3')
            cursor = conn.cursor()
            cursor.execute("SELECT count(*),systeme FROM Planete WHERE id_proprio='"+str(cherrypy.session['id'])+"' GROUP BY systeme ORDER BY count(*) ASC")
            for row in cursor:
                systeme= row[1]
            html = index_conquesty(systeme)
            return html.encode('latin1')
        
    conquesty.exposed = True
    @cherrypy.tools.sessions()
    def inscription(self):
        
            return """<html>
              <head><link rel="stylesheet" type="text/css" href="/dist/css/login.css"></head>
              <body>
               <h1>Conquesty</h1>
                <form method="post" action="log">
                  Login : <input type="text" value="" name="msg" />
                  Mot de passe : <input type="password" value="" name="mdp" />
                  Adresse mail : <input type="email" value="" name="mail" />
                  <button type="submit">Inscription</button>
                </form>
              </body>
            </html>"""
        
    inscription.exposed = True
    
    
def serveur():
    configfile=os.path.join(os.path.dirname(__file__),r"config.conf")
    application = cherrypy.tree.mount(Authentification(), '/')
    cherrypy.config.update({'server.socket_host': '0.0.0.0'} )  
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

def moteur_planete():
        max_pop()
        energie()
        hangar_metal()
        hangar_cristal()
        hangar_gaz()
        metal()
        cristal()
        gaz()
        population()
        
def moteur_conquesty():
    i=1
    while i<500:
        time.sleep(30)
        moteur_planete()

serveur = threading.Thread(None, serveur)
moteur = threading.Thread(None, moteur_conquesty)
moteur.start() 
serveur.start()
