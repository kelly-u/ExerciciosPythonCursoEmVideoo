# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1

print(f'Número: {numero}')
print(f'Antecessor: {antecessor}')
print(f'Sucessor: {sucessor}')
print(f'{antecessor} - {numero} - {sucessor}')