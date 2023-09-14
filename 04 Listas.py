import os

def menu():
	print("	------------------------------------")
	print("		  MANEJO DE LISTAS			")
	print("	------------------------------------")
	print("	1.- Agregar un elemento		")
	print("	2.- Mostrar lista			")
	print("	3.- Borrar el último elemento")
	print("	4.- Borrar lista 			")
	print("	5.- Sumar todos los elementos")
	print("	0.- Salir	\n")

def agregar(lista, a):
	lista.append(a)
	return lista

def borrarUlti(lista):
	return lista.pop()

def sumatoria(lista):
    suma = 0
    for e in lista:
        suma = suma + e
    return suma

os.system("cls")
os.system("Title LISTORTI V1.1")
lista=[]
while True:
	os.system("Color 3a")
	menu()
	op = int(input("	Ingrese una opción: "))
	if op == 0:
		break
	elif(op==1):
		os.system("cls")
		os.system("Color 3f")
		print("		RESTA	\n")
		a = int(input("Ingrese un nro a agregar: "))
		agregar(lista,a)
		print("Se agregó: ",a,"\n")
		os.system("pause")
		os.system("cls")
	elif(op==2):
		os.system("cls")
		os.system("Color 3f")
		print("		MOSTRAR LISTA	\n")
		print("La lista es: ",lista,"\n")
		os.system("pause")
		os.system("cls")
	elif(op==3):
		os.system("cls")
		os.system("Color 2f")
		print("		BORRAR ÚLTIMO ELEMENTO	\n")
		print("Borrado el: ",borrarUlti(lista),"\n")
		os.system("pause")
		os.system("cls")
	elif(op==4):
		os.system("cls")
		os.system("Color 4f")
		print("		Lista borrada	\n")
		lista=[]
		print(lista,"\n")
		os.system("pause")
		os.system("cls")
	elif(op==5):
		os.system("cls")
		os.system("Color 2f")
		print("		SUMATORIA	\n")
		print("La suma total es: ",sumatoria(lista),"\n")
		os.system("pause")
		os.system("cls")
	elif(op>=5):
		os.system("cls")
os.system("cls")
print("\nListorti v1.1\n")
os.system("pause")