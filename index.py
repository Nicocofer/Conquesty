#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 
import re
import sqlite3
from class_object.Planete import Planete

#form = cgi.FieldStorage()
def index_conquesty(systeme):
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()

    print("Content-type: text/html; charset=utf-8\n")

    #recuperation
    cursor.execute("SELECT id FROM Planete WHERE systeme="+str(systeme)+" and galaxie=1")

    liste_planete_systeme=[]
    for row in cursor:

        planete = Planete()

        planete.affichage_planete(row[0])
        liste_planete_systeme.append(planete)



        
    file = open("index.html", "r")
    html=""
    for line in file:
        if line.strip()=="<div class=\"boxP\" id=\"\"><div class=\"headP\"><div class=\"nameP\">Name planet</div><div class=\"close\" onclick=\"closebox()\"><span>X</span></div></div><div class=\"bodyP\"><div class=\"bodyP-top\"><div class=\"bodyP-left\"><div class=\"Pparam\">Type :</div><div class=\"Pparam\">Propriaitaire :</div><div class=\"Pparam\">Attaque :  <br> Defense :</div></div><div class=\"bodyP-right\"><div class=\"Pparam\">Systeme solaire : <br>Galaxie :</div><div class=\"Pparam\">Coordonnees<br> x :   / y :</div><div class=\"Pparam\">Population :</div></div></div><div class=\"bodyP-bottom\"><div class=\"Rtitle\">Ressouces de la planete</div><div class=\"ressources\"><div class=\"ressources-box\"><p id=\"metal\">metal :</p><p id=\"cristal\">cristal :</p></div><div class=\"ressources-box\"><p id=\"gaz\">gaz :</p><p id=\"energie\">energie :</p></div></div></div></div></div>":
            for planete in liste_planete_systeme:

                html= html +"<div class=\"boxP\" id=p\""+planete.id+"\"><div class=\"headP\"><div class=\"nameP\">"+planete.nom+"</div><div class=\"close\" onclick=\"closebox()\"><span>X</span></div></div><div class=\"bodyP\"><div class=\"bodyP-top\"><div class=\"bodyP-left\"><div class=\"Pparam\">Type :"+planete.type+"</div><div class=\"Pparam\">Propriaitaire :"+planete.id_proprio+"</div><div class=\"Pparam\">Attaque : "+planete.attaque+" <br> Defense :"+planete.armure+"</div></div><div class=\"bodyP-right\"><div class=\"Pparam\">Syst&egrave;me solaire : "+planete.systeme+"<br>Galaxie :"+planete.galaxie+"</div><div class=\"Pparam\">Coordonn&eacute;es<br> x : "+planete.x+"  / y : "+planete.y+"</div><div class=\"Pparam\">Population :"+planete.pop+"/"+planete.pop_max+"</div></div></div><div class=\"bodyP-bottom\"><div class=\"Rtitle\">Ressouces de la plan&egrave;te</div><div class=\"ressources\"><div class=\"ressources-box\"><p id=\"metal\">m&eacute;tal : "+planete.metal+"/"+planete.metal_max+"</p><p id=\"cristal\">cristal : "+planete.cristal+"/"+planete.cristal_max+"</p></div><div class=\"ressources-box\"><p id=\"gaz\">gaz : "+planete.gaz+"/"+planete.gaz_max+"</p><p id=\"energie\">energie :"+planete.energie+"</p></div></div></div></div></div>"
            
                   
        elif line.strip()== "<div class=\"planet type0\" id=\"\" style=\"top:30%;left:30%;\" onclick=\"openbox()\"></div>":
            
            for planete in liste_planete_systeme:
                x = planete.x
                y = planete.y
                x = float(x)
                y = float(y)
                type_planete = planete.type
                id_planete = planete.id
                if x >= 0:
                    x=50+ (x/100)
                else:
                    x=(x+500)/100
                if y >= 0:
                    y=50+ (y/100)
                else:
                    y=(y+500)/100
                html= html +"<div class=\"planet type"+str(type_planete)+"\" id=\""+ str(id_planete) +"\" style=\"top:"+str(y)+"%;left:"+str(x)+"%;\" onclick=\"openbox()\"></div>"
                    
        else:
            html= html + line
        

    return html

