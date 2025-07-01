# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.

viagemDistancia = float(input('Digite a distância da viagem em km: '))

if viagemDistancia <= 200:
    print(f'O valor total da passagem para {viagemDistancia}km é de R${viagemDistancia * 0.50:.2f}')
else:
    print(f'O valor total da passagem para {viagemDistancia}km é de R${viagemDistancia * 0.45:.2f}')
