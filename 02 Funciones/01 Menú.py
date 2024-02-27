import os

def menu():
	print("Soy el menú ")

while True:
	menu()
	op = int(input("Ingrese una opción: "))
	if op == 0:
		break
os.system("pause")