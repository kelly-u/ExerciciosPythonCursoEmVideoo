# Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos números separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = int(input('Digite um número inteiro entre 0 e 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'UNIDADE: {unidade}')
print(f'DEZENA: {dezena}')
print(f'CENTENA: {centena}')
print(f'MILHAR: {milhar}')