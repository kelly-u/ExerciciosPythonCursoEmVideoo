# Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantiade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por km rodado.

kmRodado = float(input('Digite a quantidade de km rodados: '))
qntDias = float(input('Digite a quantidade de dias que você utilizou o carro: '))

valorPagar = (kmRodado * 0.15) + (qntDias * 60)

print(f'O valor a ser pago após {kmRodado}km rodados e {qntDias} dias com o carro é de {valorPagar:.2f}.')