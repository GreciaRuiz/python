#Sumar 4 números y mostrar la suma de ellos. 
#Averiguar cuál es el mayor número de los ingresados.
c=0
suma=0
while c<4:
	nro=int(input("Ingrese un número:"))
	suma=suma+nro
	if c==0:
		mayor=nro
	else:
		if mayor<nro:
			mayor=nro
	c=c+1
print("La suma es: {} y el mayor es: {}".format(suma,mayor))

input()