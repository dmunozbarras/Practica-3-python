# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA3 - EJERCICIO 2
Escribe un programa que pida el peso y la altura de una persona y que calcule
su índice de masa corporal (imc). El imc se calcula con la fórmula
imc = peso / altura
"""
peso=float(input("Introduce su peso:"))
altura=float(raw_input("Introduce su altura:"))
imc= peso/(altura*altura)
print "Tu imc es %.2f" % (imc)
if imc<18.50:
    print"Su peso esta por debajo de lo normal"
elif imc<25:
    print"Tiene un peso normal"
elif imc<30:
    print"Tiene sobrepeso"
else:
    print"Tiene obesidad"
