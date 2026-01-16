import random
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


nomes = ["João", "Maria", "Ana", "John"]

random.shuffle(nomes)

clear()
print(f"A ordem foi {nomes} começando da esquerda para a direita!")
