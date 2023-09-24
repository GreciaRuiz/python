def comprobar(edad):
	if edad<18:
		print("No puede pasar")
	else:
		if edad>25:
			print("Puede pasar al VIP")
		else:
			print("Pasa pero no al VIP")

edad=int(input("Ingrese su edad: "))
comprobar(edad)	