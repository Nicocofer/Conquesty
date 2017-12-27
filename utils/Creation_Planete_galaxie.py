#!/usr/bin/python3
# -*- coding: utf-8 -*
import sys



from class_object.Planete import Planete

for systeme in range(3):
    planete = Planete()
    planete.creation(systeme)
