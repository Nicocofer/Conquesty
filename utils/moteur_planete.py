#!/usr/bin/python3
# -*- coding: utf-8 -*
import sqlite3
import random

def max_pop():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor_batiment = conn.cursor()
    cursor.execute("SELECT id FROM planete")
    max_pop=0
    for row in cursor.fetchall():
        cursor_batiment.execute("SELECT niveau FROM batiment WHERE id_planete='"+str(row[0])+"' and type=1")
        max_pop=0
        for bat in cursor_batiment.fetchall():
            max_pop = max_pop + (bat[0] * 100000)
        cursor.execute("UPDATE Planete SET population_max = "+str(int(max_pop))+" WHERE ID =" +str(row[0]))
        conn.commit()
        
def population():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor.execute("SELECT id, population,type,population_max FROM planete")
    
 
    for row in cursor.fetchall():
        
        pop = row[1]
        if pop >= row[3]:
            pop = row[3]
        else:
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
        
        
        cursor.execute("UPDATE Planete SET population = "+str(int(pop))+" WHERE ID =" +str(row[0]))
        conn.commit()
        
    conn.close()
                   
