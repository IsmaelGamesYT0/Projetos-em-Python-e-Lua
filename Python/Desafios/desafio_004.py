# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

algo = input("Digite algo:")


print("É alfabético?", algo.isalnum())
print("Contém apenas maiúsculas?", algo.isupper())
print("Contém apenas minúsculas?", algo.islower())
print("É númerico?", algo.isnumeric())
print("Contém espaço(s)?", algo.isspace())
print("Contém dígitos?", algo.isdigit())
print("É decimal?", algo.isdecimal())