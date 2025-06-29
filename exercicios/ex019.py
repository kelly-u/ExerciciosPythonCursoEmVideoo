# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random

contador = 1
alunos = []
while contador < 5:
    alunos.append(input(f'Digite o nome do {contador}º aluno: '))
    contador += 1

print(f'O nome do aluno escolhido foi {random.choice(alunos)}')