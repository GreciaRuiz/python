import os

def menu():
	print("	------------------------------------")
	print("			MENU			")
	print("	1.- Saludar	")
	print("	2.- Salir	\n")

os.system("cls")
os.system("Color f0")
os.system("Title Punto 4: Mi primer menú")
while True:
	menu()
	op = int(input("	Ingrese una opción: "))
	if op == 2:
		break
	elif(op==1):
		os.system("cls")
		print("Hola")
		os.system("pause")
		os.system("cls")
os.system("cls")
print("\nGracias por usar Mi programa\n")
os.system("pause")