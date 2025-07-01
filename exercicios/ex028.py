# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descrobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

numeroComputador = randint(1,5)
print(numeroComputador)

# No Python não tem o Do | While.
# Mas, posso usar o While True.
# Que dá a certeza que a instrução vai ser executada pelo menos uma vez.
# É comum utilizar aliada a um if e um break.

while True:
    numeroUsuario = int(input('Estou pensando em um número... Você consegue adivinhar? Diga qual é... '))

    if numeroUsuario == numeroComputador:
        print('Você acertou!! :)')
        break
    else:
        print('Você errou! :(')