# Estruturas Condicionais

# If | else:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print(f'\n{"-" * 3} FIM {"-" * 3}') # Pra escrever 3 vezes de cada lado.

# Condição simplificada:
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print(f'\n{"-" * 3} FIM {"-" * 3}') # Pra escrever 3 vezes de cada lado.