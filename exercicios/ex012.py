# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: R$'))
precoDesconto = preco - (preco * 5/100)

print(f'O valor do produto passou de R${preco:.2f} para R${precoDesconto:.2f} com 5% de desconto.')