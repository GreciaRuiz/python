import os

def menu():
	print("	------------------------------------------")
	print("			CALCULADORA			")
	print("	------------------------------------------")
	print("	1.- Sumar	")
	print("	2.- Restar	")
	print("	3.- Multiplicar	")
	print("	4.- Dividir	")
	print("	0.- Salir	\n")

def sumar(a,b):
	return a+b

def restar(a,b):
	return a-b

def mult(a,b):
	return a*b

def div(a,b):
	return a/b

os.system("cls")
os.system("Title CALCULADORA")
while True:
	os.system("Color f0")
	menu()
	op = int(input("	Ingrese una opción: "))
	if op == 0:
		break
	elif(op==1):
		os.system("cls")
		os.system("Color 1f")
		print("		SUMA	\n")
		a = int(input("Ingrese el primer nro: "))
		b = int(input("Ingrese el segundo nro: "))
		print("El resultado de la suma es: ",sumar(a,b),"\n")
		os.system("pause")
		os.system("cls")
	elif(op==2):
		os.system("cls")
		os.system("Color 2f")
		print("		RESTA	\n")
		a = int(input("Ingrese el primer nro: "))
		b = int(input("Ingrese el segundo nro: "))
		print("El resultado de la resta es: ",restar(a,b),"\n")
		os.system("pause")
		os.system("cls")
	elif(op==3):
		os.system("cls")
		os.system("Color 4f")
		print("		MULTIPLICACIÓN	\n")
		a = int(input("Ingrese el primer nro: "))
		b = int(input("Ingrese el segundo nro: "))
		print("El resultado de la multiplicación es: ",mult(a,b),"\n")
		os.system("pause")
		os.system("cls")
	elif(op==4):
		os.system("cls")
		os.system("Color 3f")
		print("		DIVISIÓN	\n")
		a = int(input("Ingrese el primer nro: "))
		b = int(input("Ingrese el segundo nro: "))
		print("El resultado de la división es: ",div(a,b),"\n")
		os.system("pause")
		os.system("cls")
	elif(op>=5):
		os.system("cls")
os.system("cls")
print("\nCerrado Calculadora v1.0\n")
os.system("pause")