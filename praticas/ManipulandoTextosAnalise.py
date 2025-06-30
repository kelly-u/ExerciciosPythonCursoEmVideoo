# Manipulando Textos
# Python diferencia minúsculas e maiúsculas

frase = 'Curso em Vídeo Python'
print(frase)

# len - tamanho da frase
print(len(frase)) # 21

# count (1) - conta a quantidade de vezes que um determinado caractere aparece
print(frase.count('o')) # 3

# count (2) - conta a quantidade de vezes que um determinado caractere aparece entre os caracteres 0 e 12 (13-1)
print(frase.count('o', 0, 13)) # 1

# find (1) - Vai dizer em que momento começou a String procurada ou pelo menos, a primeira vez que ela aparece.
print(frase.find('deo')) # 4

# find (2) - Com uma string que não está contida na string em questão.
print(frase.find('Android'))  # -1

# in - ele retorna um bool para afirmar ou negar se a string está contida dentro da variável 'frase'
print('Curso' in frase) # True