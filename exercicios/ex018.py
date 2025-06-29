# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin
from math import cos
from math import tan

angulo = float(input('Digite um ângulo para análise: '))

print(f'O ângulo {angulo}º tem SEN = {sin(angulo):.2f} | CO = {cos(angulo):.2f} | TA = {tan(angulo):.2f}')
