# O mesmo professor do desafio anrterior quer sortear a ordemd e apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

contador = 1
alunos = []

while contador < 5:
    alunos.append(input(f'Digite o nome do(a) {contador}º aluno(a): '))
    contador += 1

shuffle(alunos)
print(f'A nova ordem dos alunos para a apresentação = {alunos}')

