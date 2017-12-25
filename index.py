#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 
import re
import sqlite3

form = cgi.FieldStorage()

conn = sqlite3.connect('Base_conquesty.db3')
cursor = conn.cursor()

print("Content-type: text/html; charset=utf-8\n")

cursor.execute("""SELECT metal,metal_max,cristal,cristal_max,gaz,gaz_max,enregie FROM Planete""")
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
    else:
        html= html + line
    

print(html)
