import time

try:
    num1 = int(input('Digite um número inteiro positivo: '))
    
    # Verifica se o número inserido é inteiro e positivo
    if num1 <= 0:
        print('Por favor, insira apenas um número inteiro positivo!')
    else:
        soma_total = 0
        print('Começando a soma dos números pares...')
        print('=' * 40)  # Espaçamento inicial
        
        # Começo do Loop
        for i in range(1, num1 + 1):  # Começa de 1 até num1
            if i % 2 == 0:  # Verifica se o número é par
                soma_total += i  # Soma todos os números pares
                print(f'Número par: {i}')
                time.sleep(1)  # Delay entre as iterações
        
        print('-' * 20)  # Espaçamento antes do resultado
        
        # Exibe a soma dos números pares até o número inserido pelo usuário
        print(f'A soma dos números pares de 1 até {num1} é: {soma_total}')
        print('=' * 40)  # Espaçamento final

except ValueError:
    print('Insira apenas números inteiros válidos!')
