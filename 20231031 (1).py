# -*- coding: utf-8 -*-
"""20231031.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DpDttRK19UZT45kL5tV6hzkI8nVkkmOB
"""

print("hola")
print('Pablo')

print(2.1+1)
a=1
b=5.1
print(a+b)

a=input("Digite un numero ")
b=input("Digite un numero ")
a = int(a)
b = int(b)

print(a+b)

print('Area de rectangulo')
a=input("Digite base ")
b=input("Digite altura ")
a = int(a)
b = int(b)

print(a*b)

#pablo
print('Area de Circulo')
a=input("Digite el radio ")

a = int(a)
b = 3.1416

print(b*a**2)

a=input("Digite tu edad ")
a = int(a)
if a>=18:
  print("eres mayor de edad")
if a < 18:
        print("eres menor de edad")

for i in range(1,5):
  print(i)

a=input("Digite el la tabla ")
a = int(a)
for i in range(1,10):
  print(a,"X",i,"=",i*a)

#ciclo while que con 1 continue y -1 parre
a = input("Digite un numero ")
a = int(a)

while a != -1:
    print("Digite 1 para continuar o -1 para salir")
    a = input("Digite un numero ")
    a = int(a)
    if a == -1:
        break
    print(a)
    a += 1

print("¡Fin del ciclo!")

#entran mayores de edad hasta 45
edad = input("Digite tu edad ")
edad = int(edad)

if edad >= 18 and edad < 45:
    print("Puedes entrar")
else:
    print("No puedes entrar")

contador = 0

while a != -1:
  edad = input("Digite tu edad ")
  edad = int(edad)

  if edad >= 18 and edad < 45:
    print("Puedes entrar")
    contador += 1
  else:
    print("No puedes entrar")

    print("Digite 1 para continuar o -1 para salir")
    a = input("Digite un numero ")
    a = int(a)
    if a == -1:
        break

print("¡Fin del ciclo!")
print("En total", contador, "personas cumplieron con los requisitos")

#hipotenusa
import math

a = int(input("Digite base: "))
b = int(input("Digite altura: "))

hipotenusa = math.sqrt(a**2 + b**2)

print("La hipotenusa es:", hipotenusa)

# Coordenadas de las dos casas
f1=int(input("Ingrese la fila de la primera casa: "))
c1=int(input("Ingrese la columna de la primera casa"))
casa1 = (f1, c1)  # Fila 0, columna 0
f2=int(input("Ingrese la fila de la primera casa: "))
c2=int(input("Ingrese la columna de la primera casa"))
casa2 = (f2, c2)  # Fila 2, columna 3
import math
# Calculamos la distancia utilizando la fórmula de distancia euclidiana
distancia = math.sqrt((casa2[0] - casa1[0]) ** 2 + (casa2[1] - casa1[1]) ** 2)
distancia = distancia-1
# Imprimimos el resultado
print("el amor de tu vida esta a:", distancia,"casas de distancia")

#juego de ajedrez con dos torres (blanco) y (negro) que cuando una de las dos torres esten frente a frente aparesca la torre esta en peligro
# Coordenadas de las torres
torre1 = (1, 6)
torre2 = (1, 2)

# Verificar si las torres están en la misma fila o columna
if torre1[0] == torre2[0] or torre1[1] == torre2[1]:
    print("¡Alerta! Hay al menos dos torres en la misma fila o columna.")
else:
    print("No hay torres en la misma fila o columna.")

#Alfil
alfil1 = (1, 1)
alfil2 = (7, 5)

# Verificar si los alfiles están en la misma fila o columna
if abs(alfil1[0] - alfil2[0]) == abs(alfil1[1] - alfil2[1]):
    print("¡Alerta! Hay al menos dos alfiles en la misma diagonal.")
else:
    print("No hay alfiles en la misma diagonal.")