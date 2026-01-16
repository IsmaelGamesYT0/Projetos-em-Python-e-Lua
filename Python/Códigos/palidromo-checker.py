# Passo 1: Ler a entrada
texto = input("Digite uma palavra ou frase: ")

# Passo 2: Processar a entrada
# (Remover espaços e transformar em minúsculas)
texto_limpo = texto.replace(" ", "").lower()
# Passo 3: Verificar se é palíndromo
# (Comparar com a versão invertida)
if texto_limpo == texto_limpo[::-1]:
    print(f"{texto} é um Palindromo!")
else:
    print(f"{texto} Não é um Palindromo!")
          