# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

corFavorita = input('Qual sua cor favorita? ')

print(f'COR: {corFavorita} | É númerico? {corFavorita.isnumeric()} | É alfanumérico? {corFavorita.isalpha()} | Minúsculo? {corFavorita.islower()} | Maiúscula? {corFavorita.isupper()} | É printável? {corFavorita.isprintable()} | É um dígito? {corFavorita.isdigit()}')