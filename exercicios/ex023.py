# Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos números separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numeroInt = int(input('Digite um número inteiro entre 0 e 9999: '))
numero = str(numeroInt)
numero = numero.split()

if numeroInt >= 0 and numeroInt <= 9:
    print(f'Unidade: {numero[0][0]}')
    print('Dezena: 0')
    print('Centena: 0')
    print('Milhar: 0')
elif numeroInt > 9 and numeroInt <= 99:
    print(f'Unidade: {numero[0][1]}')
    print(f'Dezena: {numero[0][0]}')
    print('Centena: 0')
    print('Milhar: 0')
elif numeroInt > 99 and numeroInt <= 999:
    print(f'Unidade: {numero[0][2]}')
    print(f'Dezena: {numero[0][1]}')
    print(f'Centena: {numero[0][0]}')
    print('Milhar: 0')
elif (numeroInt > 999 and numeroInt <= 9999):
    print(f'Unidade: {numero[0][3]}')
    print(f'Dezena: {numero[0][2]}')
    print(f'Centena: {numero[0][1]}')
    print(f'Milhar: {numero[0][0]}')
else:
    print('Número fora do intervalo solicitado!')