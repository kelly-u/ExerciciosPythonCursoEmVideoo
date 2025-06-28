# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar. Considere US$1.00 = R$3.27

dinheiroReal = float(input('Quanto dinheiro em real você tem? R$'))
dinheiroDolar = dinheiroReal / 3.27

print(f'R${dinheiroReal} reais são ${dinheiroDolar:.2f} dólares.')