# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA3 - EJERCICIO 8
Escribe un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades
son. Recuerda que una gruesa son doce docenas.
"""
num1= int(raw_input ("Escribe un numero "))
gruesa= (num1/144)
docena= (num1-(gruesa*144))/12
unidad= (num1-((gruesa*144)+(docena*12)))

print "Su numero %d son %d gruesas, %d docenas y %d unidades " % (num1, gruesa, docena, unidad)
