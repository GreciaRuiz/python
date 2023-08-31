import os

def menu():
	print("	------------------------------------")
	print("		  MANEJO DE LISTAS			")
	print("	------------------------------------")
	print("	1.- Borrar lista 			")
	print("	2.- Agregar un elemento		")
	print("	3.- Mostrar lista			")
	print("	4.- Borrar el último elemento")
	print("	0.- Salir	\n")

def agregar(lista, a):
	lista.append(a)
	return lista

def borrarUlti(lista):
	return lista.pop()

os.system("cls")
os.system("Title LISTORTI V1.O")
lista=[]
while True:
	os.system("Color f0")
	menu()
	op = int(input("	Ingrese una opción: "))
	if op == 0:
		break
	elif(op==1):
		os.system("cls")
		os.system("Color 3f")
		print("		Lista borrada	\n")
		lista=[]
		print(lista,"\n")
		os.system("pause")
		os.system("cls")
	elif(op==2):
		os.system("cls")
		os.system("Color 3f")
		print("		RESTA	\n")
		a = int(input("Ingrese un nro a agregar: "))
		agregar(lista,a)
		print("Se agregó: ",a,"\n")
		os.system("pause")
		os.system("cls")
	elif(op==3):
		os.system("cls")
		os.system("Color 3f")
		print("		MOSTRAR LISTA	\n")
		print("La lista es: ",lista,"\n")
		os.system("pause")
		os.system("cls")
	elif(op==4):
		os.system("cls")
		os.system("Color 3f")
		print("		BORRAR ÚLTIMO ELEM	\n")
		print("Borrado el: ",borrarUlti(lista),"\n")
		os.system("pause")
		os.system("cls")
	elif(op>=5):
		os.system("cls")
os.system("cls")
print("\nListorti v1.0\n")
os.system("pause")