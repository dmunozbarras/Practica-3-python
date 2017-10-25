# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA3 - EJERCICIO 1
Escribe un programa que pida dos números y que escriba su media aritmética.
"""
num1=float(raw_input("introduzca un numero:"))
num2=float(raw_input("introduzca otro numero:"))
media=((num1+num2)/2.0)
print"la media de %.1f y %.1f es: %.1f" % (num1, num2, media)
