# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

# Verificando o maior
maior = num1
if num2 > num3 and num2 > num1:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

# Verificando o menor
menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print(f'Menor número = {menor} | Maior número = {maior}')