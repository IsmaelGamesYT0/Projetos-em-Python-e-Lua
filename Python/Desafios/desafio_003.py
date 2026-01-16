# Crie um programa que peça ao usuário para digitar dois números,
# e depois mostre a soma desses dois números na tela.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

print("A soma entre {} e {} é igual à {}".format(num1, num2, soma))