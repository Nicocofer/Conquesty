#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 
import re
import sqlite3

form = cgi.FieldStorage()

conn = sqlite3.connect('Base_conquesty.db3')
cursor = conn.cursor()

print("Content-type: text/html; charset=utf-8\n")

#recuperation
cursor.execute("""SELECT metal,metal_max,cristal,cristal_max,gaz,gaz_max,energie FROM Planete""")
for row in cursor:
    metal=str(row[0])
    metal_max=str(row[1])
    cristal=str(row[2])
    cristal_max=str(row[3])
    gaz=str(row[4])
    gaz_max=str(row[5])
    energie=str(row[6])


    
file = open("index.html", "r")
html=""
for line in file:
    if line.strip()=="<p id=\"metal\"></p>":
        html= html +"<p id=\"metal\">" + metal +"/"+ metal_max + "</p>"
    elif line.strip()=="<p id=\"cristal\"></p>":
        html= html +"<p id=\"cristal\">" + cristal+"/"+ cristal_max  + "</p>"
    elif line.strip()=="<p id=\"gaz\"></p>":
        html= html +"<p id=\"gaz\">" + gaz+"/"+ gaz_max  + "</p>"
    elif line.strip()=="<p id=\"energie\"></p>":
        html= html +"<p id=\"energie\">" + energie + "</p>"
    elif line.strip()== "<div class=\"planet type0\" id=\"\" style=\"top:30%;left:30%;\" onclick=\"openbox()\"></div>":
        
        cursor.execute("""SELECT x,y,type,id FROM Planete WHERE systeme=0 and galaxie=1""")
        for row in cursor:
            x = row[0]
            y = row[1]
            type_planete = row[2]
            id_planete = row[3]
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
    

print(html)
