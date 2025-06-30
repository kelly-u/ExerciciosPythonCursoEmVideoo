# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras tem ao toodo sem considerar os espaços

nome = input('Digite seu nome: ')

print(f'MAIÚSCULO: {nome.upper()}')
print(f'MINÚSCULO: {nome.lower()}')
print(f'QUANTIDADE DE LETRAS: {len(nome.replace(' ', ''))}')