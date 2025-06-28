# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$'))

salarioAumento = salario + (salario * 15/100)

print(f'O salário de R${salario:.2f}, foi aumentado para R${salarioAumento:.2f} em 15%.')