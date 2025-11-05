#Numero primo y no primo
numero = int(input("Ingrese un número entero positivo: "))
if numero == 2:
    print(f"{numero} es un número primo")
elif numero % 2 == 0 or numero <= 1:
    print(f"{numero} NO es un número primo")
else:
    i = 3
    primo = True
    limite = int(numero**0.5)
    while i <= limite and primo:
        if numero % i == 0:
            primo = False
        i += 2
    print(f"{numero} es un número primo" if primo else f"{numero} NO es un número primo")

numero_= int(input("Ingrese un entero positivo: "))
for e in range(1, numero_ + 1):
    if e % 2 != 0:
        print (e)

numero_1 = int(input("Ingrese el primer número entero positivo: "))
numero_2 = int(input("Ingrese el segundo número entero positivo: "))
suma = 0
for i in range(numero_1, numero_2 + 1):
    if i % 2 != 0:
        suma += i
print(suma)

numero_3 = int(input("Ingrese un número: "))
for e in range(numero_3, -1, -1):
    print(e)

numero_4 = int(input("Ingrese un número cualquiera: "))

for i in range(1, numero_4 + 1):
    print("*" * i)

numero_5 = int(input("Ingrese un número entero positivo: "))

for i in range(0, numero_5 + 1):
    print(i)