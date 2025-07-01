# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Digite um ano para análise (caso queira o ano atual, digite 0): '))

if ano == 0:
    ano = date.today().year # Da data de hoje, vai pegar só o ano
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')