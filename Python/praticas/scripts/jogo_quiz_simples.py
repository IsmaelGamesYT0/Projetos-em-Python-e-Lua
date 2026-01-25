# Faça um quiz sobre jogos.
import time

print('Seja Bem-vindo ao Quiz de Jogos.')
print('=' * 40)
try:
    time.sleep(2)
    print('-' * 30)
    print('Vamos então começar!')
    time.sleep(1)

    farcry = input('Qual Far Cry é considerado o melhor de todos os tempos?: ')
    farcry = farcry.lower().replace(" ", "")
    print('-' * 70)

    if farcry == 'farcry3':
        print('Certa Resposta!')
    elif farcry == 'farcry2':
        print('Quase você acertou, Far Cry 2 é considerado o 6° Melhor.')
    elif farcry == 'farcry5':
        print('Passou perto, o Far Cry 5 é considerado o 2° Melhor.')
    elif farcry == 'farcry4':
        print('Quase, o Far Cry 4 é considerado o 3° Melhor.')
    elif farcry == 'farcry6':
        print('Errou. o Far Cry 6 é considerado o 4° Melhor.')
    elif farcry == 'farcryprimal':
        print('Passou Longe. o Far Cry Primal é considerado o 5° Melhor.')
    elif farcry == 'farcry1':
        print('Desculpe, o Far Cry 1 é considerado o 7° Melhor.')
        time.sleep(2)
    else:
        print('Não entendi.')
        exit()

    time.sleep(2)
    print('-' * 60)
    print('Obrigado por jogar meu Quiz, Até mais!')
    print('=' * 40)
except ValueError:
    print(f"Ocorreu um erro!")

exit()
