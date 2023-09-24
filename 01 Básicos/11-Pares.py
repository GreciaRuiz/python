#Pedir 5 números al usuario y mostrar solamente los que sean pares
c=0
vector=[]
while c<5:
	nro=int(input("Ingrese un número: "))
	if nro % 2 == 0:
		vector.append(nro)
	c=c+1
print("Los valores pares son: ",*vector)


input()