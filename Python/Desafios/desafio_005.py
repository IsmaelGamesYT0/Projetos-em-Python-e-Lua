# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor


num = int(input("Digite um número:"))
sucessor = num + 1
antecessor = num - 1

print("Aqui vai uma tabela com o seu número, juntamente com o sucessor e antecessesor correspondente! \n")

print("Seu número é: {}, o sucessor é {} e o antecessor é {}".format(num, sucessor, antecessor))
