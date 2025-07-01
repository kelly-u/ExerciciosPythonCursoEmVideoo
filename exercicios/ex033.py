# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3 and num2 > num1:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num3 and num2 < num1:
    menor = num2
else:
    menor = num3

print(f'Menor número = {menor} | Maior número = {maior}')