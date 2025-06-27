# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Digite seu nome: ')

# 3 formas de colocar uma variável com uma string
print(f'Seja muito bem-vinda, {nome}')
print('Seja muito bem-vinda, {}'.format(nome))
print('Seja muito bem-vinda,', nome)