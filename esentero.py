#coding: utf-8
divisor=float(input("Introduzca divisor:"))
dividendo=float(input("Introduzca dividendo:"))
resultado=divisor%dividendo
if resultado==0:
	print "Es entero"
else:
	print "No es entero"
	print divisor/dividendo
