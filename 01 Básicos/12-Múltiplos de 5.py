#Pedir 5 números al usuario y mostrar solamente los 
#múltiplos de 5
c=0
cant_multiplos=0
vector=[]
while c<5:
	nro=int(input("Ingrese un número: "))
	if nro % 5 == 0:
		vector.append(nro)
		cant_multiplos=cant_multiplos+1
	c=c+1
if cant_multiplos == 0:
	print("No hay múltiplos de 5 en los nros. ingresados ")
else:
	print("Los múltiplos de 5 son: ",*vector)

input()