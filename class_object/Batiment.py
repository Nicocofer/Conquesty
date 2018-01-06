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

    def creation_batiment(self,type_bat, niv, metal, cristal, x, y):
        """

        a determiner

        """

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
