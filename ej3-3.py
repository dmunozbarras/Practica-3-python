# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA3 - EJERCICIO 3
Escribe un programa que pida una distancia en pies y pulgadas y que escriba
esa distancia en centimetros. Recuerda que un pie son doce pulgadas y
una pulgada son 2,54 cm.
"""
pies=float(raw_input("introduce pies:"))
pulgadas= float(raw_input("Introduce pulgadas"))
cm1= (((pies)*12)*2.54)
cm2= ((pulgadas)*2.54)
sumcm= (cm1+cm2)
print "los pies %.2f y las pulgadas %.2f son %.2f cm" % (pies, pulgadas, sumcm)
