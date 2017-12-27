#!/usr/bin/python3
# -*- coding: utf-8 -*
'''
Class Planete

    - recuperation planete base de donnée
    - creation de planete dans la base de donnée
    - modification de planete base de donnée
'''
import sqlite3
import random

class Planete:
    
    def __init__(self):
        self.metal = 0
        self.metal_max = 1000
        self.cristal = 0
        self.cristal_max = 1000
        self.gaz = 0
        self.gaz_max = 1000
        self.energie = 100
        self.id_proprio = 0
        self.pop = 0
        self.type = random.randrange(4)
        self.galaxie = 1
        self.systeme = self.attribution_systemes()
        self.nom = self.nom_aleatoire()
        self.armure = 0
        self.attaque = 0
        self.x=self.coord_aleatoire()
        self.y=self.coord_aleatoire()
        
    def creation(self,nb):
        
        conn = sqlite3.connect('Base_conquesty.db3')
        
        cursor = conn.cursor()
        print(self.nom)
        params=(self.nom,self.pop,self.metal,self.metal_max,self.cristal,self.cristal_max,self.gaz,self.gaz_max,self.energie,self.type,self.armure,self.attaque,self.id_proprio,self.systeme,self.galaxie,self.x,self.y)
        cursor.execute("""INSERT INTO planete(id,name,population,metal,metal_max,cristal,cristal_max,gaz,gaz_max,energie,type,armure,attaque,id_proprio,systeme,galaxie,x,y) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)""", params)
        conn.commit()
        conn.close()
    def coord_aleatoire(self):

        coord = random.randrange(500)
        if random.randrange(2)==1:
            return (coord*(-1))
        else:
            return coord
        
    def attribution_systemes(self):
        num_systeme = random.randrange(3)
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        liste_nom_base=[]
        cursor.execute("SELECT COUNT(*) FROM planete WHERE systeme =" + str(num_systeme))
        for row in cursor:
            nb_planete= row[0]
        while nb_planete == 3:
            num_systeme = random.randrange(3)
            cursor.execute("SELECT COUNT(*) FROM planete WHERE systeme =" + str(num_systeme))
            for row in cursor:
                nb_planete= row[0]
        conn.close()
        return num_systeme
    
    def nom_aleatoire(self):
        num= random.randrange(9999)
        nom = "P" + str(num)
        
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        liste_nom_base=[]
        cursor.execute("""SELECT name FROM planete""")
        for row in cursor:
            liste_nom_base.append(str(row[0]))

        while nom in liste_nom_base:
            
            num= random.randrange(9999)
            nom = "P" + str(num)
            
        conn.close()
        return nom



        
