# Crie um programa que leia um número Real quealquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um número: 6.127 -> "O número 6.127 tem a parte inteira 6."

from math import trunc

numero = float(input('Digite um número real: '))

print(f'O número {numero} tem a parte inteira {trunc(numero)}')
print(f'O número {numero} tem a parte inteira {int(numero)}')