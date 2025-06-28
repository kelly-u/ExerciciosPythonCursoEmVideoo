# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'km: {km} | hm: {hm} | dam: {dam} | m: {m} | dm: {dm} | cm: {cm}, mm: {mm}')