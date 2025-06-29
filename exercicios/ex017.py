# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt
from math import hypot

catetoOposto = float(input(f'Digite o cateto oposto: '))
catetoAdjacente = float(input(f'Digite o cateto adjacente: '))

# Forma 1 de descobrir a hipotenusa
print(f'O triângulo retângulo com CO = {catetoOposto} e CA = {catetoAdjacente}, tem a HI = {hypot(catetoOposto, catetoAdjacente):.2f}')

# Forma 2 de descobrir a hipotenusa
print(f'O triângulo retângulo com CO = {catetoOposto} e CA = {catetoAdjacente}, tem a HI = {sqrt((catetoOposto ** 2) + (catetoAdjacente ** 2)):.2f}')

# Forma 3 de descobrir a hipotenusa
print(f'O triângulo retângulo com CO = {catetoOposto} e CA = {catetoAdjacente}, tem a HI = {(catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2) :.2f}')