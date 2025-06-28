# Tipo primitivos e saída de dados - Aula #6

# string
n = input('Digite algo (string): ')
# n = str(input('Digite algo: ')) # Também funciona
print(f'{n}, | {type(n)}, | É numérico? {n.isnumeric()} | É letra? {n.isalpha()}')

# int
n1 = int(input('Digite algo (int): '))
print(f'{n1}, | {type(n1)}, | É numérico? {n1.is_integer()} ')

# float
n2 = float(input('Digite algo (float): '))
print(f'{n2}, | {type(n2)}, | É numérico? {n2.is_integer()} ')

# boolean
n3 = bool(input('Digite algo (boolean): '))
print(f'{n3}, | {type(n3)}, | É numérico? {n3.is_integer()} ')
# se escrever algo: True. Se não: False.

