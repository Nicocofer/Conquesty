#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 
import re
import sqlite3
form = cgi.FieldStorage()

conn = sqlite3.connect('Base_conquesty.db3')
cursor = conn.cursor()
print("Content-type: text/html; charset=utf-8\n")

cursor.execute("""SELECT metal,cristal,gaz,enregie FROM Planete""")
for row in cursor:
    metal=str(row[0])
    cristal=str(row[1])
    gaz=str(row[2])
    energie=str(row[3])
file = open("index.html", "r")
html=""
for line in file:
    if line.strip()=="<p id=\"metal\"></p>":
        html= html +"<p id=\"metal\">" + metal + "</p>"
    elif line.strip()=="<p id=\"cristal\"></p>":
        html= html +"<p id=\"cristal\">" + cristal + "</p>"
    elif line.strip()=="<p id=\"gaz\"></p>":
        html= html +"<p id=\"gaz\">" + gaz + "</p>"
    elif line.strip()=="<p id=\"energie\"></p>":
        html= html +"<p id=\"energie\">" + energie + "</p>"
    else:
        html= html + line
    

print(html)
