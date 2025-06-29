# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt

catetoOposto = float(input(f'Digite o cateto oposto: '))
catetoAdjacente = float(input(f'Digite o cateto adjacente: '))
hipotenusa = sqrt((catetoOposto ** 2) + (catetoAdjacente ** 2))

print(f'O triângulo retângulo com CO = {catetoOposto} e CA = {catetoAdjacente}, tem a HI = {hipotenusa}')
