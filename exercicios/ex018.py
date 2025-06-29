# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
from math import sin
from math import cos
from math import tan
from math import radians

angulo = float(input('Digite um ângulo para análise: '))

anguloRad = radians(angulo)
# transformando de graus para radianos

print(f'O ângulo {angulo}º tem SEN = {sin(anguloRad):.2f} | CO = {cos(anguloRad):.2f} | TA = {tan(anguloRad):.2f}')
