# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from time import sleep
from math import sin, cos, tan, radians
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


angulo = float(input("Digite o ângulo que você deseja:"))

radianos = radians(angulo)

seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)
clear()

print("Calculando...")
sleep(2)

clear()


print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}\n")
print(f"O Cosseno de {cosseno:.2f}\n")
print(f"E o Tangente de {tangente:.2f}")
