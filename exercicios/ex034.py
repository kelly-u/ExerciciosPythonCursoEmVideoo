# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$1250.00, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário: R$'))

if salario > 1250:
    print(f'Seu salário passou por um aumento de 10% e ficou por R${salario * 1.1:.2f}')
else:
    print(f'Seu salário passou por um aumento de 15% e ficou por R${salario * 1.15:.2f}')
'''
# Outra forma de fazer
if salario > 1250:
    print(f'Seu salário passou por um aumento de 10% e ficou por R${salario + (salario * 10/100):.2f}')
else:
    print(f'Seu salário passou por um aumento de 15% e ficou por R${salario + (salario * 15/100):.2f}')
'''