# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = input('Digite seu nome: ').strip()
nomeDividido = nome.split()

print(f'Primeiro: {nomeDividido[0]}')
print(f'Último: {nomeDividido[-1]}')
