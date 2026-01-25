#Faça um programa que leia algo pelo teclado
#e mostre na tela  todas as informações possíveis sobre ela.

n = input('Digite algo:')
print(type(n))
print('É Alfanúmerica?',n.isalnum())
print('É com letras maiuscúlas?',n.isupper())
print('É alfabetíco?',n.isalpha())
print('É númerico?', n.isnumeric())

