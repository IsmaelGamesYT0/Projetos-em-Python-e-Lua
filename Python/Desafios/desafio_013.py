# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_atual = int(input("Informe seu salário atual:"))

aumento = salario_atual * 1.15

print("Parabéns, seu salário teve um reajuste e você adquiriu um aumento de 15%, agora seu salário que antes era de R${} reais, será de R${:.2f} reais.".format(salario_atual, aumento))
