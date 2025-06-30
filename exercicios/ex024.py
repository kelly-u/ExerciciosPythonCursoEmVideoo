# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

cidade = input('Digite o nome de uma cidade: ').strip()

if 'SANTO' in cidade.upper():
    print(f'Sim! A cidade {cidade} tem "SANTO" no nome!')
else:
    print(f'Não! A cidade {cidade} tem "SANTO" no nome!')