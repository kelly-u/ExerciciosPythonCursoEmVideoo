# Exemplo de operações aritméticas com Strings. MUITO LEGAL!!

palavra = 'Oi' + 'Olá'
print(palavra)

palavra2 = 'Oi' * 5
print(palavra2)

palavra3 = '=' * 20
print(palavra3)

############################################################

print('*' * 40)

nome = input('Digite seu nome: ')
print(f'Olá, {nome:>20}'.upper()) # Alinhado a direita 20 espaços
print(f'Olá, {nome:<20}'.upper()) # Alinhado a esquerda 20 espaços
print(f'Olá, {nome:^20}'.upper()) # Alinhado no meio de 20 espaços
print(f'Olá, {nome:*>20}'.upper()) # Alinhado a direita 20 espaços com *
print(f'Olá, {nome:$<20}'.upper()) # Alinhado a esquerda 20 espaços com $
print(f'Olá, {nome:#^20}'.upper()) # Alinhado no meio de 20 espaços com #
