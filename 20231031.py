
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