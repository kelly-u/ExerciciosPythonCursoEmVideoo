# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.

print('-=' * 20)
print('ANALIZADOR DE TRIÂNGULOS')
print('-=' * 20)

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
    print('Os ângulos podem formar um triângulo!')
else:
    print('Os ângulos não podem formar um triângulo!')