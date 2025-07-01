# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.

reta1 = int(input('Digite o comprimento da primeira reta: '))
reta2 = int(input('Digite o comprimento da segunda reta: '))
reta3 = int(input('Digite o comprimento da terceira reta: '))

if reta1 + reta2 > reta3:
    if reta2 + reta3 > reta1:
        if reta1 + reta3 > reta2:
            print('Os ângulos podem formar um triângulo!')
        else:
            print('Os ângulos não podem formar um triângulo!')
    else:
        print('Os ângulos não podem formar um triângulo!')
else:
    print('Os ângulos não podem formar um triângulo!')