#Realizar la validación de una nota. La misma debe pertenecer al rango comprendido entre
#uno y diez. En caso de ingresar una nota invalida mostrar un error y pedir ingresar el número
#nuevamente hasta que ingrese un número que cumpla con la condición.

nota=int(input("Ingrese una nota: "))
while nota>10 or nota<0:
	nota=int(input("ERROR! Ingrese una nota válida: "))
print("La nota ingresada es",nota)

input()