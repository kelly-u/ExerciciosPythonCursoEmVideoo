# Manipulando Textos
# Python diferencia minúsculas e maiúsculas

frase = 'Curso em Vídeo Python'
print(frase)

# Fatiamento (1)
print(frase[9]) # Mostra o caractere 'V' que está na posição 9 -> conta com os espaços

# Fatiamento (2)
print(frase[9:13]) # Mostra os caracteres 'Vide' -> o 13 não é incluso

# Fatiamento (3)
print(frase[9:21]) # Mostra 'Vídeo Python' -> vai até o 20, por isso quando coloca 21, pega até o 'n' de Python.

# Fatiamento (4)
print(frase[9:21:2]) # Mostra de 'VdoPto' -> vai do 9 até o 20, pulando de 2 em 2.

# Fatiamento (5)
print(frase[:5]) # Mostra 'Curso'; :5 == 0:5 -> quando não tem o inicial, ele começa a partir do 0.

# Fatiamento (6)
print(frase[15:]) # Mostra 'Python'; 15: == 15:final -> quando não tem o final, ele vai até o final da String.

# Fatiamento (7)
print(frase[9::3]) # Mostra 'VePh' -> começa no 9. Como falta o número do meio, vai até o final. Pula de 3 em 3.

