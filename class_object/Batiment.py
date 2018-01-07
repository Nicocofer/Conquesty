#!/usr/bin/python3
# -*- coding: utf-8 -*

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

        cursor.execute("SELECT * FROM CoutBatiment Where type="+type_bat+" and niveau=1")
        for row in cursor:
            if metal >= row[3] and cristal >= row[4] and gaz >= row[5]:
                return True
            else:
                return False
            
    def creation_batiment(self,type_bat, metal, cristal, gaz, x, y,id_proprio,id_planete):
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        cursor_batiment = conn.cursor()
        cursor_planete = conn.cursor()
        cursor.execute("SELECT * FROM CoutBatiment Where type="+type_bat+" and niveau=1")
        for row in cursor:
            if metal >= row[3] and cristal >= row[4] and gaz >= row[5]:
                "autoriser"
                metal=metal-row[3]
                cristal=cristal-row[4]
                gaz=gaz-row[5]
                cursor_batiment.execute("INSERT INTO Batiment(id,type,niveau,id_proprio,x,y) VALUES (NULL,'"+str(type_bat)+"',1,"+str(id_proprio)+","+str(x)+","+str(y)+")")
                cursor_planete.execute("UPDATE planete SET metal="+str(metal)+" and cristal="+str(cristal)+" and gaz="+str(gaz)+" WHERE id="+str(id_planete)+"")
                conn.commit()
            else:
                "non autoriser"
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
