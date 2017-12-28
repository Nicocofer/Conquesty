#!/usr/bin/python3
# -*- coding: utf-8 -*
import sqlite3
import random

def population():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor.execute("SELECT id, population,type FROM planete")
    
 
    for row in cursor.fetchall():
        
        pop = row[1]
        if pop < 1000:
            if row[2]==3:
                pop=pop + float(pop)*0.01*random.randrange(9)
            else:
                pop=pop + float(pop)*0.01*random.randrange(4)
        else:
            if row[2]==3:
                pop=pop + float(pop)*0.001*random.randrange(9)
            else:
                pop=pop + float(pop)*0.001*random.randrange(4)
        print(pop)
        
        cursor.execute("UPDATE Planete SET population = "+str(int(pop))+" WHERE ID =" +str(row[0]))
        conn.commit()
        
    conn.close()
                   
