# Crie um programa que escreva "Olá, Mundo!" na tela.

# print("Olá, Mundo!")

import time

nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))
if idade >= 18:
    print("Você é maior de idade, Entrada Liberada!")
elif idade < 18:
    print("Você é menor de idade, ENTRADA PROIBIDA!")
else:
    print("Idade inválida!")

time.sleep(2)
print("==============================================")

print("Olá, {}! Você tem {} anos.".format(nome, idade))