#!/usr/bin/python3
# -*- coding: utf-8 -*
'''
Class Planete

    - recuperation planete base de donnée
    - creation de planete dans la base de donnée
    - modification de planete base de donnée
'''
import sqlite3


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

    def creation():
        
        conn = sqlite3.connect('Base_conquesty.db3')
        cursor = conn.cursor()
        requete="CREATE TABLE IF NOT EXISTS users( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, age INTERGER)"
