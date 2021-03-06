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
        self.pop_max = 10000
        self.type = 0
        self.galaxie = 1
        self.systeme = 0
        self.nom = ""
        self.armure = 0
        self.attaque = 0
        self.x = 0
        self.y = 0
        self.id = 0
    def creation(self,nb):
        
        conn = sqlite3.connect('Base_conquesty.db3')
        
        cursor = conn.cursor()
        print(self.nom)
        self.type = random.randrange(4)
        self.systeme = self.attribution_systemes()
        self.nom = self.nom_aleatoire()
        self.x=self.coord_aleatoire()
        self.y=self.coord_aleatoire()
        params=(self.nom,self.pop,self.pop_max,self.metal,self.metal_max,self.cristal,self.cristal_max,self.gaz,self.gaz_max,self.energie,self.type,self.armure,self.attaque,self.id_proprio,self.systeme,self.galaxie,self.x,self.y)
        cursor.execute("""INSERT INTO planete(id,name,population,population_max,metal,metal_max,cristal,cristal_max,gaz,gaz_max,energie,type,armure,attaque,id_proprio,systeme,galaxie,x,y) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)""", params)
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

    def affichage_planete(self,id_planete):
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        
        cursor.execute("""SELECT metal,metal_max,cristal,cristal_max,gaz,gaz_max,energie,x,y,type,id,name,id_proprio,attaque,armure,systeme,galaxie,population,population_max FROM Planete Where id={}""".format(id_planete))
        for row in cursor:
            self.metal=str(row[0])
            self.metal_max=str(row[1])
            self.cristal=str(row[2])
            self.cristal_max=str(row[3])
            self.gaz=str(row[4])
            self.gaz_max=str(row[5])
            self.energie=str(row[6])
            self.x = str(row[7])
            self.y = str(row[8])
            self.type = str(row[9])
            self.id = str(row[10])
            self.nom= str(row[11])
            self.id_proprio= str(row[12])
            self.attaque= str(row[13])
            self.armure= str(row[14])
            self.systeme = str(row[15])
            self.galaxie = str(row[16])
            self.pop = str(row[17])
            self.pop_max = str(row[18])

        
