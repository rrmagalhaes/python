import random

#############################################################################################
### Código Principal


def jogar():
    # Variáveis principais
    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7

    # Imprime cabeçalho
    cabecalho_forca()

    # Seleciona a palavra do arquivo base
    palavra_secreta = escolhe_palavra_secreta()

    # Impreme a quantidade de letras da palavra selecionada
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    ##### Bloco lógico responsável pela interação com o jogo
    while(not enforcou and not acertou):
        # Solicita entrada da letra
        chute = entrada_chute()

        # Verifica se a letra faz parte da palavra | testes lógicos
        if(chute in palavra_secreta):
            chute_correto(chute, palavra_secreta, letras_acertadas)
            print(f'Acertou, ainda restam {tentativas} tentativas!')
        else:
            erros += 1
            tentativas -= 1
            desenha_forca(erros, tentativas)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(25 * '-')
        print(letras_acertadas)

    # Imprime resultado caso vença ou perda
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo")

#############################################################################################
## Funções lógicas auxiliares


def chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def entrada_chute():
    while (True):
        chute = input("\n"+"Qual letra? ").strip().upper()
        if (chute == ""):
            print("Digite uma letra!")
        elif (len(chute) > 1):
            print("Digite apenas uma letra!")
        else:
            return chute
            break

def escolhe_palavra_secreta():
    palavras = []
    arquivo = open("palavras.txt", "r")
    # with open("palavras.txt") as arquivo:

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

#############################################################################################
## Funções auxiliares de impressão


def cabecalho_forca():
    print(35 * "*")
    print("*** Bem vindo ao jogo da Forca! ***")
    print(35 * "*")

def desenha_forca(erros, tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print(f'Errado, ainda restam {tentativas} tentativas!')
    print()

def imprime_mensagem_vencedor():
    print("\n"+"Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("\n"+"Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


# Valida execução local
if(__name__ == "__main__"):
    jogar()