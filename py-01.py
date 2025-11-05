
p,q,r =10,20,30
print(p,q,r)   

"""
i = 10
print("Esto va antes del bucle")
while i >= 1:
    print(i)
    i -= 1
print("Esto va despues del bucle")

numero = 8
i = 0
limite = 12 
while i <= 12:
    print (f"{numero} x {i} = {numero * i}")
    i = i + 1

       """
"""

mi_lista = ["carro", "moto", "avion", "barco"]
i = 0
while i < len(mi_lista):
    print(mi_lista[i])
    i += 1  
    
  

i = 0
while i<=100:
    if i%5 ==0:
        print(i)
    i +=1

     
for elemento in mi_lista:
    print(elemento)
  

i = 0
while i < 5:
    print(i)
    i += 2
else:
    print("El bucle ha terminado")


for e in mi_lista:
    print(e)    
else:
    print("sali del for")

    """
"""
mi_lista = [1,2,3,4,5,6,7,8,9,10]

for i in range(8):
    print(i)

for i in range(2,10):
    print(i)



for i in range(1,19,2):
    print(i)

    

for i in range(10,0,-1):
    print(i)

    
mi_lista = ["carro", "moto", "avion", "barco"]
for elemento in mi_lista:
    pass
print("Hola")

"""
for i in range(20+1):
    if i % 3 == 0:
        continue
    print(i)

while True:
    nombre = input("Ingrese su nombre ")
    if nombre == 'ana':
        continue
    print(nombre)