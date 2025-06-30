# Manipulando Textos
# Python diferencia minúsculas e maiúsculas

frase = 'Curso em Vídeo Python'
print(frase)

# split - divisão nas strings considerando seus espaços ou outros delimitadores.
dividido = (frase.split())

print(dividido)  # ['Curso', 'em', 'Vídeo', 'Python']

######### DICAAAAA #########
# Posso usar quando quiser só uma palavra da string
print(dividido[0]) # Curso
print(dividido[1]) # em
print(dividido[2]) # Vídeo
print(dividido[3]) # Python

######### DICAAAAA #########

# Para pegar a última palavra
print(dividido[-1]) # Python

######### DICAAAAA #########

# Para pegar a última letra da última palavra
print(dividido[-1][-1]) # n

######### DICAAAAA #########
# Para pegar a última letra de qualquer palavra
print(dividido[2][-1]) # Vídeo -> o

######### DICAAAAA #########
# Posso pegar a letra específica da palavra
print(dividido[0][2]) # Curso -> r

