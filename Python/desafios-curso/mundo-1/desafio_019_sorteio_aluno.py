from time import sleep
import random
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


nomes = ["João", "Maria", "Ana", "John"]


def selectRandom(nomes):
    return random.choice(nomes)


print(f"O aluno sorteado para limpar o quadro foi... \n")
sleep(3)
clear()

print("Sorteando...")
sleep(3)
clear()

print(
    f"Parabéns {selectRandom(nomes)}, você ganhou o sorteio e terá que limpar o quadro!"
)
