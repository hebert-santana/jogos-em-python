# importando pacotes
import random

# criando variáveis do game
tentativas = 4
letras_escolhidas = []
nomes = ['alien', 'amelie', 'arrival', 'avatar', 'bambi', 'braveheart', 'casablanca', 'coco', 'dumbo', 'fargo', 
         'fantasia', 'frozen', 'gladiator', 'gravity', 'hereditary', 'hugo', 'interstellar', 'jumanji', 'matilda', 
         'memento', 'moana', 'mulam', 'psycho', 'scream', 'shrek', 'tangled', 'us', 'vertigo', 'whiplash', 'zootopia']

nome_aleatorio = random.choice(nomes)
nome_oculto = "_" * len(nome_aleatorio)

    
# atualizar palavra oculta
def atualizar_oculta(oculta, letra, palavra):
    novo_nome_oculto = ""
    for i in range(len(palavra)):
        if palavra[i] == letra:
            novo_nome_oculto += letra
        else:
            novo_nome_oculto += oculta[i]
    return novo_nome_oculto


print('\n\033[33m================================= JOGO DA FORCA EM PYTHON =================================\033[0m')
print('Adivinhe o nome do filme:')

# loop inicial do jogo
while True:
    print(nome_oculto)
    print(f'\nTentativas restantes: {tentativas}')
    print(f'Letras escolhidas: {letras_escolhidas}')
    letra = input("Escolha uma letra: ")

    # verificando as letras escolhidas
    if letra in letras_escolhidas:
        print(f'Já digitou a letra "{letra}" antes!')
    else:
        letras_escolhidas.append(letra)
        if letra in nome_aleatorio:
            print('\033[32mAcertou!\033[0m')
            nome_oculto = atualizar_oculta(nome_oculto, letra, nome_aleatorio)
            print(f'Novo nome oculto = {nome_oculto}')
            # verificando se a palavra inteira foi descoberta
            if "_" not in nome_oculto:
               break
               
        elif letra not in nome_aleatorio:
            print('\033[31mErrou!\033[0m')
            tentativas = tentativas - 1
            # verificando fim de jogo
            if tentativas == 0:
                print("        ________")
                print("       |/       |")
                print("       |       (_)")
                print("       | !!!  \033[31mPERDEU\033[0m  !!!")
                print("       |       /|\\")
                print("       |        |")
                print("       |       / \\")
                print("      _|________")
                print(f"\n      \033[31mO nome do filme era: {nome_aleatorio}\033[0m\n")
                break

