#!/usr/bin/python3
# -*- coding: utf-8 -*
import sqlite3
import random

def population():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor.execute("SELECT id, population FROM planete")
    
 
    for row in cursor.fetchall():
        
        pop = row[1]
        pop=pop + float(pop)*0.01
        
        
        cursor.execute("UPDATE Planete SET population = "+str(int(pop))+" WHERE ID =" +str(row[0]))
        conn.commit()
        
    conn.close()
                   
