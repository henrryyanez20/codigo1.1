#Método de las Series (Basilea)
import math

suma = 0
for valor in range(1, 1000):
    suma = suma + (1 / valor ** 2)

pi = math.sqrt(suma * 6)
print(f'El valor de pi desde python es : {pi}')