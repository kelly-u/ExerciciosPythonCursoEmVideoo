# Manipulando Textos
# Python diferencia minúsculas e maiúsculas

frase = 'Curso em Vídeo Python'
print(frase)

# replace - Substitui uma string por outra. Mas, a substituição é secundária, não é diretamente na variável.
print(frase.replace('Python', 'Android')) # Curso em Vídeo Android

# upper - Deixa toda a string em maiúscula. Mas, a substituição é secundária, não é diretamente na variável.
print(frase.upper()) # CURSO EM VÍDEO PYTHON

# lower - Deixa toda a string em minúscula. Mas, a substituição é secundária, não é diretamente na variável.
print(frase.lower()) # curso em vídeo python

# capitalize - Transforma só a primeira letra da string em maiúscula e o resto em minúscula. Mas, a substituição é secundária, não é diretamente na variável.
print(frase.capitalize())

# title - Transforma cada primeira palavra da string em maiúscula. Ele faz isso através dos espaços. A cada espaço, ele faz um capitalize de cada palavra.
print(frase.title())
