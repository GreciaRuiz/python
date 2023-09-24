#Pedir 5 números al usuario y mostrar solamente los 
#múltiplos de 5
c=0
vector=[]
while c<5:
	nro=int(input("Ingrese un número: "))
	if nro % 5 == 0:
		vector.append(nro)
	c=c+1
print("Los múltiplos de 5 son: ",*vector)


input()