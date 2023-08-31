import time
import os

def llenar(lista,cadena):
	r = 0
	for e in lista:
		if e == cadena:
			r = r+1
	if r == 0:
		lista.append(cadena)

os.system("Color f0")
os.system("cls")
os.system("Title Cadenas")
lista=[]
c = 0
print("\n")
while c<4:
	cadena = input("Ingrese un nombre: ").capitalize()
	if c==0:
		lista.append(cadena)
	else:
		llenar(lista,cadena)
	c = c+1
print(lista, "\n" )

time.sleep(1)
os.system("pause")