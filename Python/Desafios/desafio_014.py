# Conversor de Temperatura - Celsius para Fahrenheit

from time import sleep
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()

print(
    "Olá, Caro usúario, Seja Bem-vindo ao meu programa de conversão de temperaturas! \n"
)
sleep(5)
clear()

print("Este programa converte Celsius em Fahrenheit, \n")
sleep(5)
clear()

print(
    " e logo, logo, irá ter um update que permite mais conversões, espero que goste do programa!"
)
sleep(4)
clear()

temperatura_em_celsius = float(
    input("Por favor, insira a temperatura em Graus Celsius! Exemplo(32.5): ")
)

fahrenheit = (temperatura_em_celsius * 9 / 5) + 32

print(f"Sua temperatura em Fahrenheit é de {fahrenheit:.2f}°F")
sleep(4)
clear()

print("Obrigado por usar meu programa, até mais!")
sleep(5)

exit()
