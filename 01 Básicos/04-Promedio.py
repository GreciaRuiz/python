def verificar(n1,n2):
	prom=(n1+n2)/2
	if prom<6:
		c="Desaprobado. Promedio {}".format(prom)
	elif prom<8:
		c="Aprobado. Promedio {}".format(prom)
	else:
		c="Promocionado. Promedio {}".format(prom)
	return c


n1=float(input("Ingrese la primera nota: "))
n2=float(input("Ingrese la segunda nota: "))
print("Alumno:",verificar(n1,n2))

input()