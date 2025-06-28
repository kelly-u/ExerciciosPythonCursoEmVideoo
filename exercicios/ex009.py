# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite um número inteiro para a tabuada: '))

print('-' * 12)
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

print('-' * 12)