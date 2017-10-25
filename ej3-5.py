# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA3 - EJERCICIO 5
Escribe un programa que pida una temperatura en grados Fahrenheit y que escriba esa
temperatura en grados Celsius. La relación entre grados Celsius (C) y grados Fahrenheit (F) es la
siguiente:
F - 32 = 1,8 * C
"""
fh= float(raw_input("Escriba la temperatura en farenheit "))
cel= ((fh-32)/1.8)
print "La temperatura en %.2f farenheit es %.2f en Celsius" % (fh, cel)
