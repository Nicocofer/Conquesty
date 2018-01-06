#!/usr/bin/python3
# -*- coding: utf-8 -*
import sqlite3
import random

def hangar_metal():
    """

    Calcul de la metal max pour chaque planete en fonction de leurs batiments

    max metal = somme de (niv * 10 000)

    """
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor_batiment = conn.cursor()
    cursor.execute("SELECT id FROM planete")
    max_metal=0
    for row in cursor.fetchall():
        cursor_batiment.execute("SELECT niveau FROM batiment WHERE id_planete='"+str(row[0])+"' and type=3")
        max_metal=0
        for bat in cursor_batiment.fetchall():
            max_metal = max_metal + (bat[0] * 10000)
        cursor.execute("UPDATE Planete SET metal_max = "+str(int(max_metal))+" WHERE ID =" +str(row[0]))
        conn.commit()
    conn.close()
    
def hangar_cristal():
    """

    Calcul de la cristal max pour chaque planete en fonction de leurs batiments

    max cristal = somme de (niv * 10 000)

    """
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor_batiment = conn.cursor()
    cursor.execute("SELECT id FROM planete")
    max_cristal=0
    for row in cursor.fetchall():
        cursor_batiment.execute("SELECT niveau FROM batiment WHERE id_planete='"+str(row[0])+"' and type=5")
        max_cristal=0
        for bat in cursor_batiment.fetchall():
            max_cristal = max_cristal + (bat[0] * 10000)
        cursor.execute("UPDATE Planete SET cristal_max = "+str(int(max_cristal))+" WHERE ID =" +str(row[0]))
        conn.commit()
    conn.close()
    
def hangar_gaz():
    """

    Calcul de la gaz max pour chaque planete en fonction de leurs batiments

    max gaz = somme de (niv * 10 000)

    """
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor_batiment = conn.cursor()
    cursor.execute("SELECT id FROM planete")
    max_gaz=0
    for row in cursor.fetchall():
        cursor_batiment.execute("SELECT niveau FROM batiment WHERE id_planete='"+str(row[0])+"' and type=7")
        max_gaz=0
        for bat in cursor_batiment.fetchall():
            max_gaz = max_gaz + (bat[0] * 10000)
        cursor.execute("UPDATE Planete SET gaz_max = "+str(int(max_gaz))+" WHERE ID =" +str(row[0]))
        conn.commit()
    conn.close()
    
def max_pop():
    """

    Calcul de la population max pour chaque planete en fonction de leurs batiments

    max pop = somme de (niv * 100 000)

    """
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
    conn.close()
    
def metal():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor_batiment = conn.cursor()
    cursor.execute("SELECT id, metal,type,metal_max,energie FROM planete")
    for row in cursor.fetchall():
        if row[4] > 0:
            cursor_batiment.execute("SELECT niveau FROM batiment WHERE id_planete='"+str(row[0])+"' and type=2")
            metal_a_ajouter=0
            for bat in cursor_batiment.fetchall():
                metal_a_ajouter = metal_a_ajouter + (bat[0] * 1)
                
            if row[1] >= row[3]:
                metal = row[3]
            else:
                metal = metal_a_ajouter + row[1]
                
            cursor.execute("UPDATE Planete SET metal = "+str(int(metal))+" WHERE ID =" +str(row[0]))
            conn.commit()
    conn.close()
    
def cristal():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor_batiment = conn.cursor()
    cursor.execute("SELECT id, cristal,type,cristal_max,energie FROM planete")
    for row in cursor.fetchall():
        if row[4] > 0:
            cursor_batiment.execute("SELECT niveau FROM batiment WHERE id_planete='"+str(row[0])+"' and type=4")
            cristal_a_ajouter=0
            for bat in cursor_batiment.fetchall():
                cristal_a_ajouter = cristal_a_ajouter + (bat[0] * 1)
                
            if row[1] >= row[3]:
                cristal = row[3]
            else:
                cristal = cristal_a_ajouter + row[1]
                
            cursor.execute("UPDATE Planete SET cristal = "+str(int(cristal))+" WHERE ID =" +str(row[0]))
            conn.commit()
    conn.close()
    
def gaz():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor_batiment = conn.cursor()
    cursor.execute("SELECT id, gaz,type,gaz_max,energie FROM planete")
    for row in cursor.fetchall():
        if row[4] > 0:
            cursor_batiment.execute("SELECT niveau FROM batiment WHERE id_planete='"+str(row[0])+"' and type=6")
            gaz_a_ajouter=0
            for bat in cursor_batiment.fetchall():
                gaz_a_ajouter = gaz_a_ajouter + (bat[0] * 1)
                
            if row[1] >= row[3]:
                gaz = row[3]
            else:
                gaz = gaz_a_ajouter + row[1]
                
            cursor.execute("UPDATE Planete SET gaz = "+str(int(gaz))+" WHERE ID =" +str(row[0]))
            conn.commit()
    conn.close()

def energie():
    conn = sqlite3.connect('Base_conquesty.db3')
    cursor = conn.cursor()
    cursor_batiment = conn.cursor()
    cursor.execute("SELECT id, energie FROM planete")
    for row in cursor.fetchall():
        cursor_batiment.execute("SELECT niveau,type FROM batiment WHERE id_planete='"+str(row[0])+"'")
        energie = 0
        for bat in cursor_batiment.fetchall():
            if bat[1] == 8:
                energie = energie + (bat[0] * 10)
            else:
                energie = energie - (bat[0] * 10)
        cursor.execute("UPDATE Planete SET energie = "+str(energie)+" WHERE ID =" +str(row[0]))
        conn.commit()
    conn.close()
    
def population():
    """

    Calcul de la population pour chaque planete

    """
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
                   
