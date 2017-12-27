#!/usr/bin/python3
# -*- coding: utf-8 -*

from class_object.Planete import Planete

for systeme in range(9):
    if systeme != 1 :
        planete = Planete()
        planete.creation(systeme)
