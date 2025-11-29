import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

print("Bem vindo à entrevista!")
time.sleep(3)
clear()

print("A entrevista consistirá em 20 perguntas de múltipla escolha, \n")
time.sleep(3)
clear()

print("cada uma com 4 alternativas (A, B, C, D). \n")
time.sleep(3)
clear()

print("Ao final, você irá saber se você passou ou não na entrevista. \n")
time.sleep(3)
clear()

nome = input("Primeiramente, qual o seu nome?")
time.sleep(1.5)
clear()

print("Boa sorte! e vamos começar!")
time.sleep(2)
clear()


print("Começando...")
time.sleep(3)
clear()

print("Começou!")
time.sleep(1.7)
clear()


linguagens = {    
    "A": "Python",
    "B": "C++",
    "C": "Assembly",
    "D": "Java"
}

for letra, nome in linguagens.items():
    print(f"{letra}: {nome}")

while True:

   pergunta1 = input("Qual linguagem de programação listada acima é mais recomendada para iniciantes? \n")

   if pergunta1.upper() == "A":
    print("Correto! Python é uma linguagem com sintaxe simples e de fácil aprendizado para iniciantes.")
    break

   elif pergunta1.upper() == "B":
    print("Incorreto. C++ é mais complexo para iniciantes.")
    
   elif pergunta1.upper() == "C":
    print("Incorreto. Assembly é uma linguagem de baixo nível e difícil para iniciantes.")
    
   elif pergunta1.upper() == "D":
    print("Incorreto. Java tende a ser mais complexa principalmente se não tiver experiência prévia.")
    
   else:
    print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()
    

