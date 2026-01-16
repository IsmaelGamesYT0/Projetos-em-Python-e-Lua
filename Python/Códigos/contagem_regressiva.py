# Escreva um programa em Python que peça ao usuário para inserir um número inteiro positivo. O programa deve, então, contar regressivamente a partir desse número até 1, exibindo cada número na contagem.
import time

try:
    # Aqui é onde o usúario insere um número inteiro para a contagem regressiva.
    num = int(input('Digite um número inteiro:'))

    # Aqui verifica se o valor inserido é positivo.
    if num <= 0:
        print('Por favor insira um número positivo!')
    else:
        print('Contagem Regressiva:')

        # Começo do Loop.
        for i in range(num, 0, -1):
            # Espaçamento.
            print('-' * 5)
            # Exibe a contagem regressiva do número inserido até (1).
            print(i)
            time.sleep(1)

        # Espaçamento.
        print('=' * 20)

        # Agradecimentos por usar o programa.
        print('Contagem Regressiva concluída, Obrigado por usar meu programa!')

        print('=' * 20)  # Espaçamento final.

except ValueError:
    print('Por favor insira um número inteiro válido!')
    exit()  # Sair do programa