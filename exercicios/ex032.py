# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano: '))

if ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
elif ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} o não é bissexto!')