# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Informe o valor em Metros:"))

cm = metros * 100
mm = metros * 1000

print("Seu valor em Metros é {}m, em centímetros  é {} e em milímetros é {}mm".format(metros, cm, mm))


