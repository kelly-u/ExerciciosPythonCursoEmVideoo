# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa deve custar R$7.00 por cada km acima do limite.

velocidadeCarro = float(input('Digite a velocidade do carro: '))

if velocidadeCarro > 80:
    excessoVelocidade = velocidadeCarro - 80
    multa = 7.00 * excessoVelocidade

    print(f'Seu carro foi multado em R${multa:.2f} por ter passado {excessoVelocidade}km/h do limite de velocidade de 80km/h')
else:
    print('Muito bem, dirija com segurança!')