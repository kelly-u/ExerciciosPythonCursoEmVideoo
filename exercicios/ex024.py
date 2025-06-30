# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

cidade = input('Digite o nome de uma cidade: ')
if ((cidade.upper()).find('SANTO')) == 0:
    resultado = f'Sim! A cidade {cidade} tem "SANTO" no nome!'
else:
    resultado = f'Não! A cidade {cidade} tem "SANTO" no nome!'

print(resultado)