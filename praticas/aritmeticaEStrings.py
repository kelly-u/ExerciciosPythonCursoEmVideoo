# Exemplo de operações aritméticas com Strings. MUITO LEGAL!!

palavra = 'Oi' + 'Olá'
print(palavra)

palavra2 = 'Oi' * 5
print(palavra2)

palavra3 = '=' * 20
print(palavra3)

############################################################

print('\n','*' * 40, '\n')

nome = input('Digite seu nome: ')
print(f'Olá, {nome:>20}'.upper()) # Alinhado a direita 20 espaços
print(f'Olá, {nome:<20}'.upper()) # Alinhado a esquerda 20 espaços
print(f'Olá, {nome:^20}'.upper()) # Alinhado no meio de 20 espaços
print(f'Olá, {nome:*>20}'.upper()) # Alinhado a direita 20 espaços com *
print(f'Olá, {nome:$<20}'.upper()) # Alinhado a esquerda 20 espaços com $
print(f'Olá, {nome:#^20}'.upper()) # Alinhado no meio de 20 espaços com #

############################################################

print('\n','*' * 40, '\n')

# Quebrar a linha no meio do print
print(f'Olá! \n Meu nome é {nome}')

# Continuar na mesma linha, mesmo com 2 prints diferentes
print('Eu gosto muito da cor amarelo e', end=' ') # Colar espaço dentro do end é bom pq ele dá o espaço de um print pra outro.
print('eu gostaria muuuuuuito de ganhar flores amarelas! s2')

print('Oi', end='>>>') # O que é colocado dentro do end, ele coloca entre um print e outro.
print('tudo bem?')