#!/usr/bin/python3
# -*- coding: utf-8 -*
import sqlite3

class Batiment:


    def __init__(self):
        self.id = 0
        self.type = 0
        self.niv = 0
        self.id_planete =0
        self.x = 0
        self.y = 0
        
    def autoriser_construction(self,type_bat, metal, cristal, gaz, x, y,id_proprio,id_planete):
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM CoutBatiment Where type="+str(type_bat)+" and niveau=1")
        for row in cursor:
            if int(metal) >= int(row[3]) and int(cristal) >= int(row[4]) and int(gaz) >= int(row[5]):
                return True
            else:
                return False
            
    def creation_batiment(self,type_bat, metal, cristal, gaz, x, y,id_proprio,id_planete):
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        cursor_batiment = conn.cursor()
        cursor_planete = conn.cursor()
        cursor.execute("SELECT * FROM CoutBatiment Where type="+str(type_bat)+" and niveau=1")
        for row in cursor:
            if int(metal) >= int(row[3]) and int(cristal) >= int(row[4]) and int(gaz) >= int(row[5]):
                
                metal=int(metal) - int(row[3])
                cristal=int(cristal) - int(row[4])
                gaz=int(gaz) - int(row[5])
                cursor_batiment.execute("INSERT INTO Batiment(id,type,niveau,id_planete,x,y) VALUES (NULL,'"+str(type_bat)+"',1,"+str(id_planete)+","+str(x)+","+str(y)+")")
                cursor_planete.execute("UPDATE planete SET metal="+str(metal)+" WHERE id="+str(id_planete))
                cursor_planete.execute("UPDATE planete SET cristal="+str(cristal)+" WHERE id="+str(id_planete))
                cursor_planete.execute("UPDATE planete SET gaz="+str(gaz)+" WHERE id="+str(id_planete))
                conn.commit()
                return "autoriser"
            else:
                return"non autoriser"
        conn.close()
    def attribution_batiment(self,id_batiment):
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        
        cursor.execute("""SELECT * FROM Batiment Where id={}""".format(id_batiment))
        for row in cursor:
            self.id = row[0]
            self.type = row[1]
            self.niv = row[2]
            self.id_planete = row[3]
            self.x = row[4]
            self.y = row[5]
        conn.close()
