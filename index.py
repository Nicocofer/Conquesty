#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 
import re
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

metal="15"

file = open("index.html", "r")
html=""
for line in file:
    if line.strip()=="<p id=\"metal\">mÃ©tal</p>":
        html= html +"<p id=\"metal\">mÃ©tal " + metal + "</p>"
    else:
        html= html + line
    

print(html)
