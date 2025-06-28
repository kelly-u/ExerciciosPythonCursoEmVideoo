# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$'))

salarioAumento = salario + (salario * 0.15)

print(f'O salário de R${salario}, foi aumentado para R${salarioAumento} em 15%.')