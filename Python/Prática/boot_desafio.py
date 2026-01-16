from time import sleep
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


nome = input("Qual é o seu nome? ")
sleep(2)

clear()

horas_estudadas = float(input("Quantas horas você estudou hoje? "))
sleep(2)

clear()

print(f"Boa {nome}, você estudou {horas_estudadas} horas hoje!. Amanhã é +1% 🚀")
