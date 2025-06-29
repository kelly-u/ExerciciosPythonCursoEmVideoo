import math
#importação de toda a biblioteca math

numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
# sqrt = gerar a raiz quadrada

print(f'A raiz quadrada de {numero} é {raiz:.1f}')

print(f'A raiz quadrada de {numero} é {math.ceil(raiz)}.')
# ceil = arredondar pra cima

print(f'A raiz quadrada de {numero} é {math.floor(raiz)}.')
# floor = arredondar pra baixo