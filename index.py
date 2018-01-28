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



    reprisehtml=True
    file = open("index.html", "r")
    html=""
    for line in file:
        if line.strip()=="<div class=\"boxP\" id=\"\">" and reprisehtml:
            for planete in liste_planete_systeme:

               
                html = html + """

			<div class="boxP" id="p{0}">
				<div class="headP">
					<div class="nameP">{1}</div>
					<div class="close" onclick="closebox()"><span>X</span></div>
				</div>
				
				<!-- Partie info plan&eacute;taire -->
				<div class="bodyP"><div class="bodyP-top">
					<div class="bodyP-left">
						<div class="Pparam">Type : {2}</div>
						<div class="Pparam">Propriaitaire : {3}</div>
						<div class="Pparam">Attaque : {4}<br> Defense : {5}</div>
					</div>
					<div class="bodyP-right">
						<div class="Pparam">Systeme solaire : {6}<br>Galaxie : {7}</div>
						<div class="Pparam">Coordonnees<br> x :  {8} / y : {9}</div>
						<div class="Pparam">Population : {10}/{11}</div>
					</div>
				</div>
				<div class="bodyP-bottom">
					<div class="Rtitle">Ressouces de la planete</div>
					<div class="ressources">
						<div class="ressources-box">
							<p id="metal">metal : {12}/{13}</p>
							<p id="cristal">cristal : {14}/{15}</p>
						</div>
						<div class="ressources-box">
							<p id="gaz">gaz : {16}/{17}</p>
							<p id="energie">energie : {18}</p>
						</div>
					</div>
				</div>
			</div>


			<!-- Partie construction plan&eacute;taire -->
			<div class="bodyC">
				<div class="Rtitle">Construction Plan&eacute;taire</div>
				<div class="bodyP-top bodyC-top">
					<div class="bodyP-left ">

					
		""".format(planete.id,planete.nom,planete.type,planete.id_proprio,planete.attaque,planete.armure,planete.systeme,planete.galaxie,planete.x,planete.y,planete.pop,planete.pop_max,planete.metal,planete.metal_max,planete.cristal,planete.cristal_max,planete.gaz,planete.gaz_max,planete.energie)
                cursor.execute("SELECT * FROM Batiment WHERE id_planete="+str(planete.id))
                i=0
                for row in cursor:
                    if i == 5:
                        html=html +"</div><div class=\"bodyP-right\">"
                        html=html + "<div class=\"Pparam terrain\">"+str(row[1])+"</div>"
                    else:
                        html=html + "<div class=\"Pparam terrain\">"+str(row[1])+"</div>"
                    i=i+1
                if i<=5 and i!=0:
                    html=html +"</div><div class=\"bodyP-right\">"
                terrain_vierge= 10-i
                for terrain in range(terrain_vierge):
                    if terrain == 5:
                        html=html +"</div><div class=\"bodyP-right\">"
                        html=html + "<div class=\"Pparam terrain\"></div>"
                    else:
                        html=html + "<div class=\"Pparam terrain\"></div>"
                html=html +"""          
					</div>
				</div>
			</div>
			

			<!--Partie Menu plan&eacute;taire -->
			<div class="onglets">
				<ul>
					<li id='menuinfos'><p>Infos</p></li>
					<li id='menuconstruire'><p>Construire</p></li>
					<li id='menuchantierspatial'><p>Chantier Spatial</p></li>	
				</ul>
			</div></div>"""

            reprisehtml=False
            html =html + "</div>"
        elif line.strip()== "<div class=\"right\" >":
            reprisehtml=True
            html= html + line
        elif line.strip()== "<div class=\"planet type0\" id=\"\" style=\"top:30%;left:30%;\" onclick=\"openbox()\"></div>" and reprisehtml:
            
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
                    
        elif reprisehtml:
            html= html + line
        else:
            pass
        

    return html

