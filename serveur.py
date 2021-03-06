#!/usr/bin/python3
# -*- coding: utf-8 -*
import http.server
import threading
import os
import time
from utils.moteur_planete import population, max_pop, hangar_metal, metal, hangar_gaz, hangar_cristal, cristal, gaz, energie
from index import index_conquesty
from class_object.Batiment import Batiment
from class_object.Planete import Planete
import sqlite3
import cherrypy

class Authentification(object):
    @cherrypy.tools.sessions()
    def index(self):
        cherrypy.session['user'] = ""
        cherrypy.session['mdp'] = ""
        cherrypy.session['id'] = ""
        file = open("login.html", "r")
        html=""
        for line in file:
            html = html + line
        return html.encode('latin1')
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
            file = open("login.html", "r")
            html=""
            for line in file:
                if line.strip()== "<p class=\"novalide\"></p>":
                    html = html + "<p class=\"novalide\">Login ou mot de passe non valide</p>"
                else:
                    html = html + line
            return html.encode('latin1')
    log.exposed = True
    
    @cherrypy.tools.sessions()
    def conquesty(self):
            conn = sqlite3.connect('Base_conquesty.db3')
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT count(*),systeme FROM Planete WHERE id_proprio='"+str(cherrypy.session['id'])+"' GROUP BY systeme ORDER BY count(*) ASC")
                for row in cursor:
                    systeme= row[1]
                html = index_conquesty(systeme)
                return html.encode('latin1')
            except:
                html = index_conquesty(0)
                return html.encode('latin1')
            else:
                html = index_conquesty(0)
                return html.encode('latin1')
    conquesty.exposed = True
    @cherrypy.tools.sessions()
    def inscription(self):
        
            return """<html>
              <head><link rel="stylesheet" type="text/css" href="/dist/css/login.css"></head>
              <body>
               <h1>Conquesty</h1>
                <form method="post" action="inscriptionbase">
                  Login : <input type="text" value="" name="msg" />
                  Mot de passe : <input type="password" value="" name="mdp" />
                  Adresse mail : <input type="email" value="" name="mail" />
                  <button type="submit">Inscription</button>
                </form>
              </body>
            </html>"""
        
    inscription.exposed = True
    def inscriptionbase(self,msg,mdp,mail):
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Joueur(id,name,mdp,mail,credit) VALUES (NULL,'"+str(msg)+"','"+str(mdp)+"','"+str(mail)+"',0)")
        conn.commit()
        conn.close()
        return """<html>
              <head><link rel="stylesheet" type="text/css" href="/dist/css/login.css"></head>
              <body>
               <p>Merci pour votre inscription. <a href="index">Se connecter</a></p>
              </body>
            </html>"""
        
    inscriptionbase.exposed = True
    
    @cherrypy.tools.sessions()
    def batiment(self,id_planete):
        #affichage batiment
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        html="Batiment present sur la planete<br/><br/>"
        #try:
            
        cursor.execute("SELECT * FROM Batiment WHERE id_planete="+str(id_planete))
        for row in cursor:
            html=html + " Type: "+str(row[1])+" niv : "+str(row[2])+"<br/>"
            
        #except:
            #html= "Pas de batiment sur cette planete <br/>"
        #else:
            #html= "Pas de batiment sur cette planete <br/>"
        html=html+"<br/><br/>Construction:<br/><br/>"
        planete = Planete()
        planete.affichage_planete(id_planete)
        
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CoutBatiment WHERE niveau='1'")
        listebat=[]
        
        for bat in cursor:
            batiment= Batiment()
            batiment.type = bat[1]
            batiment.niveau = 1
            listebat.append(batiment)
        for bati in listebat:
            if bati.autoriser_construction(bati.type, planete.metal, planete.cristal, planete.gaz, 0, 0,cherrypy.session['id'],id_planete):
                html=html +" type: "+ str(bati.type) +" niv:" + str(bati.niveau)+ " <a href=construire?id_planete="+str(id_planete)+"&typebati="+str(bati.type)+">Construire</a> <br/>"
            else:
                html=html +" type: "+ str(bati.type) +" niv:" + str(bati.niveau)+ " Pas assez de ressources <br/>"
        html=html+"<br/><br/>Couts Batiments:<br/><br/>"        
        cursor_coutbatiment = conn.cursor()
        cursor_coutbatiment.execute("SELECT * FROM CoutBatiment")
        for bat in cursor_coutbatiment:
            html =html + "Type : " +str(bat[1])+ " Niveau : "+str(bat[2])+" Metal : " +str(bat[3])+" Crstal : "+str(bat[4])+" Gaz : " +str(bat[5])+"<br/>"
        return html
        
    batiment.exposed = True
    
    @cherrypy.tools.sessions()
    def construire(self,id_planete,typebati):
        batiment= Batiment()
        batiment.type = typebati
        batiment.niveau = 1

        planete = Planete()
        planete.affichage_planete(id_planete)
        
        html = batiment.creation_batiment(batiment.type, planete.metal, planete.cristal, planete.gaz, 0, 0,cherrypy.session['id'],id_planete)
        return html
        
    construire.exposed = True
    
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
