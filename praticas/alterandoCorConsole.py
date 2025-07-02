print('\033[0;30;41mOlá, Mundo')   # style none, text white, back red
print('\033[4;33;44mOlá, Mundo')   # style underline, text yellow, back blue
print('\033[1;35;43mOlá, Mundo')   # style bold, text purple, back yellow
print('\033[30;42mOlá, Mundo')     # style none, text white, back green
print('\033[mOlá, Mundo')          # padrão do terminal - no meu terminal, fica toodo preto
print('\033[7;30mOlá, Mundo')      # style none, text black, back white

#Retirando a faixa até o final
print('\033[33;41mOlá, Mundo\033[m')   # style bold, text vermelho, back yellow

# Todos são opicionais
# 1 - style (estilo)
'''
    0 none
    1 bold
    4 underline
    7 negative
'''
# 2 - text (texto)
'''
    30 branco
    31 vermelho
    32 verde
    33 amarelo
    34 azul
    35 roxo
    36 magenta
    37 cinza
'''
# 3 - back (plano de fundo)
'''
    40 branco
    41 vermelho
    42 verde
    43 amarelo
    44 azul
    45 roxo
    46 magenta
    47 cinza 
'''