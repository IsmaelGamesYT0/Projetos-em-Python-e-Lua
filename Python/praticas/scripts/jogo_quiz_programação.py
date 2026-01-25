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

#-------------------------------------------------------------------------------------------------------------

# Armazenamento das altenativas em um dicionário

alternativa_1 = {    
    "A": "Python",
    "B": "C++",
    "C": "Assembly",
    "D": "Java"
}

alternativa_2 = {
    "A": "Ambiente de Programação Online",
    "B": "Ferramentas de Teste de Jogos",
    "C": "Ambiente de Desenvolvimento Integrado",
    "D": "Editor de Gráficos"
}

alternativa_3 = { 
    "A": "echo()",
    "B": "print()",
    "C": "display()",
    "D": "show()"
}

alternativa_4 = {
    "A": "Unity",
    "B": "Unreal Engine",
    "C": "Godot",
    "D": "Construct"
}

alternativa_5 = {
    "A": "Um código que nunca termina",
    "B": "Um erro de compilação",
    "C": "Um jogo que nunca acaba",
    "D": "Uma função que não retorna nada"
}

alternativa_6 = {
    "A": "Um erro no código",
    "B": "Um persongaem jogável",
    "C": "Uma função especial",
    "D": "Uma otimização"
}

alternativa_7 = {
    "A": "Lua",
    "B": "Python",
    "C": "C++",
    "D": "Java"
}

alternativa_8 = {
    "A": "Frames por segundo",
    "B": "Funções por script",
    "C": "Falhas por segundo",
    "D": "Fases por segundo"
}

alternativa_9 = {
    "A": "Stack",
    "B": "Queue",
    "C": "Array",
    "D": "HashMap"
}

alternativa_10 = {
    "A": "HTML",
    "B": "JavaScript",
    "C": "CSS",
    "D": "Python"
}

alternativa_11 = {
    "A": "Inteligência Artificial",
    "B": "Arte Interativa",
    "C": "Asset Import",
    "D": "Animação Integrada"
}

alternativa_12 = {
    "A": "C++",
    "B": "JavaScript",
    "C": "PHP",
    "D": "Ruby"
}

alternativa_13 = {
    "A": "RigidBody",
    "B": "Collider",
    "C": "Animator",
    "D": "MeshRenderer"
}

alternativa_14 = {
    "A": "&&",
    "B": "||",
    "C": "!=",
    "D": "=="
}

alternativa_15 = {
    "A": "Interrope o loop",
    "B": "Reinicia o loop",
    "C": "Ignora uma interação",
    "D": "Duplica o loop"
}

alternativa_17 = {
    "A": "int",
    "B": "string",
    "C": "float",
    "D": "bool"
}

alternativa_18 = {
    "A": "Git",
    "B": "VSCode",
    "C": "Blender",
    "D": "Photoshop"
}

alternativa_19 = {
    "A": "Personagem 2D ou imagem",
    "B": "Som",
    "C": "Física",
    "D": "Iluminação"
}

alternativa_20 = {
    "A": "Comentar o código explicando sua função",
    "B": "Copiar o código sem entender",
    "C": "Ignorar erros",
    "D": "Nome aleatórios para variáveis"
}

#-------------------------------------------------------------------------------------------------------------

# Área das perguntas

for letra, nome in alternativa_1.items():
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
    
#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_2.items():
    print(f"{letra}: {nome}")


while True:
    pergunta2 = input("Na programação, o que significa 'IDE'? ")

    if pergunta2.upper() == "C":
        print("Correto! Uma IDE combina editor, compilador e ferramentas de debug em um só lugar.")
        break
    
    elif pergunta2.upper() == "A":
        print("Incorreto! Nem todo ambiente online é uma IDE.")

    elif pergunta2.upper() == "B":
        print("Incorreto! Uma IDE faz muito mais que testar.")

    elif pergunta2.upper() == "D":
        print("Incorreto! IDE foca em programação, não edição de gráficos.")
    
    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_3.items():
    print(f"{letra}: {nome}")

while True:
    pergunta3 = input("Qual dessas funções é usada para exibir texto na tela em Python? ")

    if pergunta3.upper() == "B":
        print("Correto! A função print() exibe texto ou resultado de váriaveis no console em Python.")
        break

    elif pergunta3.upper() == "A":
        print("Incorreto! echo() é usado em shell, não em Python.")

    elif pergunta3.upper() == "C":
        print("Incorreto! display() Só funciona em notebooks como Jupyter.")

    elif pergunta3.upper() == "D":
        print("Incorreto! show() não é uma função padrão em Python.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_4.items():
    print(f"{letra}: {nome}")

while True:
    pergunta4 = input("Qual dessas é uma engine de desenvolvimento de jogos amplamente utilizada? ")

    if pergunta4.upper() == "B":
        print("Correto! Unreal é muito usado em jogos AAA por seus gráficos avançados e ferramentas poderosas.")
        break

    elif pergunta4.upper() == "A":
        print("Incorreto! Unity é mais usada para jogos indie ou 2D.")

    elif pergunta4.upper() == "C":
        print("Incorreto! Godot é leve e focada em projetos indie.")

    elif pergunta4.upper() == "D":
        print("Incorreto! Construct é voltada para jogos 2D simples e drag-and-drop.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_5.items():
    print(f"{letra}: {nome}")

while True:
    pergunta5 = input("O que é um 'loop infinito' na programação? ")

    if pergunta5.upper() == "A":
        print("Correto! Um loop infinito é um ciclo que nunca termina, geralmente por falta de condição de parada.")
        break

    elif pergunta5.upper() == "B":
        print("Incorreto! Um erro de compilação impede o código de rodar, não cria loops infinitos.")

    elif pergunta5.upper() == "C":
        print("Incorreto! Um jogo pode ter fases intermináveis, mas isso não é um loop infinito.")

    elif pergunta5.upper() == "D":
        print("Incorreto! Uma função que não retorna nada é chamada de void, não um loop infinito.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_6.items():
    print(f"{letra}: {nome}")

while True:
    pergunta6 = input("O que é um 'bug' na programação? ")

    if pergunta6.upper() == "A":
        print("Correto! Um bug é um erro ou falha no código que causa comportamento inesperado.")
        break
    
    elif pergunta6.upper() == "B":
        print("Incorreto! Um personagem jogável é chamado de 'player' ou 'avatar', não um bug.")
    
    elif pergunta6.upper() == "C":
        print("Incorreto! Uma função especial pode ser qualquer coisa, mas não é um bug.")
    
    elif pergunta6.upper() == "D":
        print("Incorreto! Uma otimização melhora o desempenho, não é um bug.")
    
    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_7.items():
    print(f"{letra}: {nome}")

while True:
    pergunta7 = input("Qual linguagem é usada no Roblox para scripts? ")

    if pergunta7.upper() == "A":
        print("Correto! No Roblox os scripts são feitos em Luau, uma variação de Lua(5.1) feita para o Roblox.")
        break

    elif pergunta7.upper() == "B":
        print("Incorreto! Python é usado em várias áreas, mas não é usada para scripts no Roblox.")

    elif pergunta7.upper() == "C":
        print("Incorreto! C++ é usado para desenvolvimento de jogos, mas não no Roblox.")

    elif pergunta7.upper() == "D":
        print("Incorreto! Java não é compatível com o Roblox.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_8.items():
    print(f"{letra}: {nome}")

while True:
    pergunta8 = input("O que significa 'FPS' no contexto de jogos? ")

    if pergunta8.upper() == "A":
        print("Correto! FPS significa quantas imagens são exibidas por segundo em um jogo.")
        break
    
    elif pergunta8.upper() == "B":
        print("Incorreto! Não existe esse conceito.")
    
    elif pergunta8.upper() == "C":
        print("Incorreto! Falhas por segundo não é o significado de FPS.")
    
    elif pergunta8.upper() == "D":
        print("Incorreto! Fases por segundo não tem sentido como métrica.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_9.items():
    print(f"{letra}: {nome}")

while True:
    pergunta9 = input("Qual estrutura funciona como fila (FIFO)?")

    if pergunta9.upper() == "B":
        print("Correto! Queue mantém a ordem de chegada, primeiro a entrar, primeiro a sair.")
        break

    elif pergunta9.upper() == "A":
        print("Incorreto! Stack é pilha, LIFO (último a entrar, primeiro a sair).")

    elif pergunta9.upper() == "C":
        print("Incorreto! Array é só uma lista de elementos.")

    elif pergunta9.upper() == "D":
        print("Incorreto! Estrutura chave-valor, não fila.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_10.items():
    print(f"{letra}: {nome}")

while True:
    pergunta10 = input("Qual linguagem estrutura o conteúdo de páginas web? ")

    if pergunta10.upper() == "A":
        print("Correto! HTML define texto, links, imagens e estrutura da página.")
        break

    elif pergunta10.upper() == "B":
        print("Incorreto! CSS estiliza o conteúdo, não estrutura.")

    elif pergunta10.upper() == "C":
        print("Incorreto! JavaScript controla comportamento, não estrutura.")

    elif pergunta10.upper() == "D":
        print("Incorreto! Python não é usado no front-end diretamente.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_11.items():
    print(f"{letra}: {nome}")

while True:
    pergunta11 = input("O que significa 'AI' em desenvolvimento de jogos? ")

    if pergunta11.upper() == "A":
        print("Correto! AI refere-se à inteligência artificial que controla o comportamento dos NPCs.")
        break

    elif pergunta11.upper() == "B":
        print("Incorreto! Arte interativa não tem relação com AI.")

    elif pergunta11.upper() == "C":
        print("Incorreto! Asset import só importa recursos, não controla lógica.")

    elif pergunta11.upper() == "D":
        print("Incorreto! Animação integrada não é o significado de AI.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_12.items():
    print(f"{letra}: {nome}")

while True:
    pergunta12 = input("Qual linguagem compilada e rápida é usada em jogos pesados? ")

    if pergunta12.upper() == "A":
        print("Correto! C++ é usada em jogos AAA e motores pesados como Unreal Engine.")
        break

    elif pergunta12.upper() == "B":
        print("Incorreto! JavaScript é interpretada e mais lenta para jogos complexos.")

    elif pergunta12.upper() == "C":
        print("Incorreto! PHP é usado no back-end, voltada para web, não jogos.")

    elif pergunta12.upper() == "D":
        print("Incorreto! Ruby é mais usado no back-end com frameworks como Rails.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_13.items():
    print(f"{letra}: {nome}")

while True:
    pergunta13 = input("Na Unity, qual componente aplica física a objetos? ")

    if pergunta13.upper() == "A":
        print("Correto! RigidBody aplica gravidade, massa, colisões e força realista.")
        break
    
    elif pergunta13.upper() == "B":
        print("Incorreto! Collider apenas detecta colisões, não aplica física.")
    
    elif pergunta13.upper() == "C":
        print("Incorreto! Animator controla animações, não física.")

    elif pergunta13.upper() == "D":
        print("Incorreto! MeshRenderer renderiza a malha, não aplica física.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_14.items():
    print(f"{letra}: {nome}")

while True:
    pergunta14 = input("Qual operador lógico significa “E” ? ")

    if pergunta14.upper() == "A":
        print("Correto! && é o operador lógico 'E', que exige ambas as condições verdadeiras.")
        break
    elif pergunta14.upper() == "B":
        print("Incorreto! || é o operador lógico 'OU', não 'E'.")

    elif pergunta14.upper() == "C":
        print("Incorreto! != Compara diferença.")

    elif pergunta14.upper() == "D":
        print("Incorreto! == Compara igualdade.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_15.items():
    print(f"{letra}: {nome}")

while True:
    pergunta15 = input("O que faz o comando 'break' em loops? ")

    if pergunta15.upper() == "A":
        print("Correto! 'break' interrompe o loop atual imediatamente.")
        break

    elif pergunta15.upper() == "B":
        print("Incorreto! 'break' não reinicia o loop, apenas interrompe.")
    
    elif pergunta15.upper() == "C":
        print("Incorreto! 'break' não ignora interações, para isso é usado 'continue'.")

    elif pergunta15.upper() == "D":
        print("Incorreto! 'break' não duplica o loop.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_17.items():
    print(f"{letra}: {nome}")

while True:
    pergunta17 = input("Qual tipo armazena verdadeiro/falso em C#? ")

    if pergunta17.upper() == "D":
        print("Correto! 'bool' armazena valores booleanos: true ou false.")
        break

    elif pergunta17.upper() == "A":
        print("Incorreto! 'int' armazena números inteiros.")

    elif pergunta17.upper() == "B":
        print("Incorreto! 'string' armazena texto.")
    
    elif pergunta17.upper() == "C":
        print("Incorreto! 'float' armazena números decimais.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_18.items():
    print(f"{letra}: {nome}")

while True:
    pergunta18 = input("Qual ferramenta faz versionamento de código? ")

    if pergunta18.upper() == "A":
        print("Correto! Git é usado para controle de versão e colaboração em projetos de código.")
        break

    elif pergunta18.upper() == "B":
        print("Incorreto! VSCode é um editor de código, não uma ferramenta de versionamento.")

    elif pergunta18.upper() == "C":
        print("Incorreto! Blender é uma ferramenta de modelagem 3D, não versionamento.")
    
    elif pergunta18.upper() == "D":
        print("Incorreto! Photoshop é um editor de imagens, não versionamento.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_19.items():
    print(f"{letra}: {nome}")

while True:
    pergunta19 = input("O que é um sprite em jogos? ")

    if pergunta19.upper() == "A":
        print("Correto! Um sprite é uma imagem 2D usada para personagens ou objetos em jogos.")
        break

    elif pergunta19.upper() == "B":
        print("Incorreto! Som é áudio, não um sprite.")

    elif pergunta19.upper() == "C":
        print("Incorreto! Física é a simulação de movimento, não um sprite.")

    elif pergunta19.upper() == "D":
        print("Incorreto! Iluminação é o efeito de luz, não um sprite.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)    
    clear()

#-------------------------------------------------------------------------------------------------------------

for letra, nome in alternativa_20.items():
    print(f"{letra}: {nome}")

while True:
    pergunta20 = input("Qual é uma boa prática ao programar? ")

    if pergunta20.upper() == "A":
        print("Correto! Facilita leitura, manutenção e entendimento do código futuramente.")
        break

    elif pergunta20.upper() == "B":
        print("Incorreto! Copiar sem entender não ajuda no aprendizado.")

    elif pergunta20.upper() == "C":
        print("Incorreto! Ignorar erros pode levar a problemas maiores.")
    
    elif pergunta20.upper() == "D":
        print("Incorreto! Nomes aleatórios dificultam a leitura do código.")

    else:
        print("Resposta inválida. Por favor, somente escolha A, B, C ou D.")
    time.sleep(2)
    clear()

print(f"Parabéns por completar a entrevista, {nome}!")
time.sleep(2)
clear()


