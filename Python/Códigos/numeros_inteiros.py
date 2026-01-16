# Escreva um programa que peça ao usuário para inserir uma lista de números inteiros, termine a entrada quando o usuário digitar 0, e então exiba a soma de todos os números inseridos (exceto o 0).


numeros = []
while True:
    num = int(input('Digite qualquer número inteiro (0 para terminar): '))
    if num == 0:
        break
    numeros.append(num)

soma = sum(numeros)

print('A soma de todos os números inseridos é {}'.format(soma))
