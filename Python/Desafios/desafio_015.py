# Aluguel de carros

from time import sleep
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


dias_alugados = int(input("Quantos dias alugados?: "))
clear()
km_rodados = float(input("Quantos KM's rodados?: "))
clear()
pagamento = (dias_alugados * 60)(km_rodados + 0.15)

print("Calculando...")
sleep(3)
clear()

print(
    f"Você alugou {dias_alugados} dias e rodou {km_rodados:.2f}km \n"
    f"Total a pagar: R${pagamento} reais"
)
