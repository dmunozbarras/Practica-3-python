# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA3 - EJERCICIO 6
Escribe un programa que pida una cantidad de segundos y que escriba cuántos minutos
son.
"""
num1= int(raw_input("Escriba los segundos "))
minutos= (num1/60)
segundos= (num1-(minutos*60))
print "Los segundos %d son %d minutos y %d segundos" % (num1, minutos, segundos)
