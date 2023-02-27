# Importando pacotes
import random
import os
import sys
import time

# comando para limpar a tela
limpa_tela = os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela com cls no Windows e o comando clear em outros sistemas

def reiniciar_game():
    # limpa a tela e reinicia o programa
    limpa_tela # limpa a tela com cls no Windows e o comando clear em outros sistemas
    os.execv(sys.executable, ['python'] + sys.argv) # reinicia o programa

# print no início do game
print("\n --------------------------- \n JOGO DA FORCA EM PYTHON \n \n Adivinhe o nome do filme: \n \n")

# lista de nomes de filmes
nomes = ['alien', 'amelie', 'arrival', 'avatar', 'bambi', 'braveheart', 'casablanca', 'coco', 'dumbo', 'fargo', 'fantasia', 'frozen', 'gladiator', 'gravity', 'hereditary', 'hugo', 'interstellar', 'jumanji', 'matilda', 'memento', 'moana', 'mulam', 'psycho', 'scream', 'shrek', 'tangled', 'us', 'vertigo', 'whiplash', 'zootopia']

# escolhendo um nome aleatório da lista de nomes de filmes
nome_aleatorio = random.choice(nomes)

# criando o nome oculto para exibir a quantidade de letras no prompt
nome_oculto = "_" * len(nome_aleatorio)

# criando variáveis do game
tentativas = 4
letras_escolhidas = []
game_over = False

# função para atualizar palavra oculta ao acertar a letra
def atualizar_oculta(oculta, letra, palavra):
    novo_nome_oculto = ""
    for i in range(len(palavra)):
        # se a letra na posição i for igual a letra que o usuário escolheu
        if palavra[i] == letra:
            # adiciona a letra na exibição do novo nome oculto
            novo_nome_oculto += letra
        else:
            # se não, adiciona o caracter "_" no novo nome oculto
            novo_nome_oculto += oculta[i]
            # retorna o novo nome oculto após as verificações
    return novo_nome_oculto

# loop inicial do jogo
while game_over != True:
    print(nome_oculto)
    print("\nTentativas restantes: ", tentativas)
    print("Letras escolhidas: ", letras_escolhidas)
    letra = input("Escolha uma letra: ")

    # verificando as letras escolhidas
    if letra in letras_escolhidas:
        print("Burro! Já digitou essa letra antes!")
        time.sleep(2)
    else:
        letras_escolhidas.append(letra)
        if letra in nome_aleatorio:
            print("Acertô uma letra Mizeravi!")
            # atualizando o nome oculto
            nome_oculto = atualizar_oculta(nome_oculto, letra, nome_aleatorio)
            print("Novo nome oculto = ", nome_oculto)
        # verificando se a palavra inteira foi descoberta
            if "_" not in nome_oculto:
               print("Ganhou! É treta! É treta!")
               game_over = True
        elif letra not in nome_aleatorio:
            print("Faustão: 'ERRRROOOUUU!!!!")
            tentativas = tentativas - 1
            # verificando fim de jogo
            if tentativas == 0:
                print("  ________")
                print(" |/       |")
                print(" |       (_)")
                print(" | !!! FOI DECEPAAAAAADOOO !!!")
                print(" |       /|\\")
                print(" |        |")
                print(" |       / \\")
                print("_|________")
                print("\n Não, cara. Que loucura! Como vc é burro! \n\n A nome do filme era: ", nome_aleatorio)
                game_over = True

# aguardar 5 segundos
time.sleep(5)
# reiniciar o game
reiniciar_game()
