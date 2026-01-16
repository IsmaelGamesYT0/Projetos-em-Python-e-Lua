# Crie um algoritmo que leia um número e mostre seu dobro, tiplo e raiz quadrada

num = int(input("Digite um número:"))

dobro = num * 2
triplo = num * 3
raiz = num ** 0.5

print("Segue abaixo o seu número, com dobro,tiplo e raiz! \n")
print("Seu número é: {}, Seu dobro é {}, Seu triplo é {} e sua raiz é {:.3f}".format(num, dobro, triplo, raiz))
