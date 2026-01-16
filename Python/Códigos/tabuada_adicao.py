# Escreva um programa em Python que peça ao usuário para inserir um número. Depois, some esse número com todos os números de 1 a 10 e exiba o resultado.

# Aqui é onde o usúario insere o número para a soma.
num = int(input('Insira um número:'))

print('=' * 15) # Espaçamento para melhorar a Legibilidade.

# Começo do loop para a soma.
for i in range (1, 11):
   
   # Cálculo da soma.
    soma = num + i
    
    # Exibição da soma de todos os números de 1 a 10.
    print(f'{num} + {i} = {soma} ')
    
print('=' * 15)  #Espaçamento final.
