# Estruturas Condicionais

# If | else (exemplos da aula #10)

nome = input('Qual é o seu nome? ').strip()
if nome.upper() == 'KELLY':
    print('Que nome lindo você tem!!')
else:
    print('Seu nome é tão normal...')
print(f'Bom dia, {nome}!!')

########################################

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Sua média foi: {media:.2f}')

if media >= 6:
    print('Sua média foi boa!! Parabéns!')
else:
    print('Sua média foi ruim. Estude mais!!')

########################################

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Sua média foi {media:.2f}.')

print('Parabéns!' if media >= 6 else 'Estude mais!')