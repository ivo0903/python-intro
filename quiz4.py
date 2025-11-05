
#1
numero_1 = int(input("Ingrese primer número: "))
numero_2 = int(input("Ingrese segundo número: "))
numero_3 = int(input("Ingrese un tercer número: "))

mayor = numero_1
if numero_2 > mayor:
    mayor = numero_2
if numero_3 > mayor:
    mayor = numero_3

print(mayor)


#2
anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año ingresado es bisiesto")
else:
    print("El año ingresado NO es bisiesto")
    

#3
angulo_1 = int(input("Ingrese el primer ángulo del triángulo: "))
angulo_2 = int(input("Ingrese el segundo ángulo del triángulo: "))
angulo_3 = int(input("Ingrese el tercer ángulo del triángulo: "))

if (angulo_1 + angulo_2 + angulo_3 == 180) and (angulo_1 > 0) and (angulo_2 > 0) and (angulo_3 > 0) and (angulo_1 < 180) and (angulo_2 < 180) and (angulo_3 < 180):
    print("Es un triángulo válido")
else:
    print("NO es un triángulo válido")

    
#4
caracter = input("Ingrese un caracter: ")

if caracter.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("El caracter ingresado es una vocal")
else:
    print("El caracter ingresado NO es una vocal")

#5
nota = float(input("Ingrese una nota entre 0 y 5: "))

if nota < 0 or nota > 5:
    print("Nota inválida")
elif nota >= 0 and nota < 2:
    print("Nota deficiente")
elif nota >= 2 and nota < 3:
    print("Nota insuficiente")
elif nota >= 3 and nota < 4.5:
    print("Nota aceptable")
elif nota >= 4.5 and nota <= 5:
    print("Nota sobresaliente")

#6
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")