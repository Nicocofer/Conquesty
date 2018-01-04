#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 
import re
import sqlite3
from class_object.Planete import Planete

#form = cgi.FieldStorage()
def index_conquesty():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()

    print("Content-type: text/html; charset=utf-8\n")

    #recuperation
    cursor.execute("""SELECT id FROM Planete WHERE systeme=1 and galaxie=1""")

    liste_planete_systeme=[]
    for row in cursor:

        planete = Planete()

        planete.affichage_planete(row[0])
        liste_planete_systeme.append(planete)



        
    file = open("index.html", "r")
    html=""
    for line in file:
        if line.strip()=="<p id=\"metal\"></p>":
            html= html +"<p id=\"metal\">" + liste_planete_systeme[1].metal +"/"+ liste_planete_systeme[1].metal_max + "</p>"
        elif line.strip()=="<p id=\"cristal\"></p>":
            html= html +"<p id=\"cristal\">" + liste_planete_systeme[1].cristal+"/"+ liste_planete_systeme[1].cristal_max  + "</p>"
        elif line.strip()=="<p id=\"gaz\"></p>":
            html= html +"<p id=\"gaz\">" + liste_planete_systeme[1].gaz+"/"+ liste_planete_systeme[1].gaz_max  + "</p>"
        elif line.strip()=="<p id=\"energie\"></p>":
            html= html +"<p id=\"energie\">" + liste_planete_systeme[1].energie + "</p>"
        elif line.strip()== "<div class=\"boxP\" id=\"\"><div class=\"headP\"><div class=\"nameP\">Name planet</div><div class=\"close\" onclick=\"closebox()\"><span>X</span></div></div></div>":
               for planete in liste_planete_systeme:
                   id_planete = planete.id
                   nom_planete = planete.nom
                   html= html + "<div class=\"boxP\" id=\"p"+id_planete+"\"><div class=\"headP\"><div class=\"nameP\">"+nom_planete+"</div><div class=\"close\" onclick=\"closebox()\"><span>X</span></div></div></div>"
                   
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

