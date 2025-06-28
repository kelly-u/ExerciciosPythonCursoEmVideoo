# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintála. Sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Digite a largura da parede (em m): '))
altura = float(input('Digite altura da parede (em m): '))

area = largura * altura

litros = area / 2

print(f'A quantidade de litros necessários para pintar uma parede de {largura}m X {altura}m são {litros}l de tinta.')

