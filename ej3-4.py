# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA3 - EJERCICIO 4
Escribe un programa que pida una temperatura en grados Celsius y que escriba esa temperatura
en grados Fahrenheit. La relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente:
F - 32 = 1,8 * C
"""
celsius=float(raw_input("Introduzca una temperatura en grados Celsius "))
Fahrenheit= (((celsius)*1.8)+32)
print "La temperatura %.2f en Celsius es %.2f en Fahrenheit  " % (celsius, Fahrenheit)
