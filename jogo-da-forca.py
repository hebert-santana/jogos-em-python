import random
print("--------------------------- \n JOGO DA FORCA EM PYTHON \n \n Adivinhe o apelido do pênis: \n \n")

nomes = ['braulio', 'ganso', 'jeba', 'mastro', 'pau',
         'pemba', 'pingola', 'pinto', 'pomba', 'rola', 'trolha']
# escolhendo um nome aleatório
nome_aleatorio = random.choice(nomes)
nome_oculto = "_" * len(nome_aleatorio)
# variáveis do jogo
tentativas = 4
letras_escolhidas = []
game_over = False

# função para atualizar palavra oculta ao acertar a letra


def atualizar_oculta(oculta, letra, palavra):
    nova_palavra_oculta = ""
    for i in range(len(palavra)):
        if palavra[i] == letra:
            nova_palavra_oculta += letra
        else:
            nova_palavra_oculta += oculta[i]
    return nova_palavra_oculta

# função para desenhar a forca
def forca(tentativas):
    vidas = 4 - tentativas
    if vidas == 0:
        print("  ________")
        print(" |/       |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|________")
    elif vidas == 1:
        print("  ________")
        print(" |/       |")
        print(" |       (_)")
        print(" |")
        print(" |")
        print(" |")
        print("_|________")
    elif vidas == 2:
        print("  ________")
        print(" |/       |")
        print(" |       (_)")
        print(" |       /|")
        print(" |")
        print(" |")
        print("_|________")
    elif vidas == 3:
        print("  ________")
        print(" |/       |")
        print(" |       (_)")
        print(" |       /|\\")
        print(" |        |")
        print(" |       / \\")
        print("_|________")
        

# loop inicial do jogo
while game_over != True:
    forca(tentativas)
    print(nome_oculto)
    print("\n Tentativas restantes: ", tentativas)
    print("Letras escolhidas: ", letras_escolhidas)
    letra = input("Escolha uma letra: ")

    # verificando as letras escolhidas
    if letra in letras_escolhidas:
        print("Burro! Já digitou essa letra antes!")
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
                print("\n Não, cara. Que loucura! Como vc é burro! \n A nome do pênis era: ", nome_aleatorio)
                game_over = True


