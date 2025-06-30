# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome

nome = input('Digite seu nome: ')

if 'SILVA' in nome.upper():
    print(f'Sim! {nome} tem "SILVA" no nome!')
else:
    print(f'Não! {nome} não tem "SILVA" no nome!')