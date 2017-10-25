# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA3 - EJERCICIO 7
Escribe un programa que pida una cantidad de segundos y que escriba cuántas
horas y minutos son.
"""
num1= int(raw_input("Escriba los segundos "))
horas= (num1/3600)
minutos= (num1-(horas*3600))/60
segundos= (num1-((horas*3600)+(minutos*60)))

print "los segundos %d son %d horas, %d minutos y %d segundos" % (num1, horas, minutos, segundos)
