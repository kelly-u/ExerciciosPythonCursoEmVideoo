from math import sqrt
from math import ceil
from math import floor

# importação de funções específicas da biblioteca math
# importações assim ajudam na memória, já que só importo aquilo que eu prepciso.

numero = int(input('Digite um número: '))
raiz = sqrt(numero) # não preciso usar 'math.' :O
# sqrt = gerar a raiz quadrada

print(f'A raiz quadrada de {numero} é {raiz:.1f}')

print(f'A raiz quadrada de {numero} arredondada pra cima é {ceil(raiz)}.') # não preciso usar 'math.' :O
# ceil = arredondar pra cima

print(f'A raiz quadrada de {numero} arredondada pra baixo é {floor(raiz)}.') # não preciso usar 'math.' :O
# floor = arredondar pra baixo