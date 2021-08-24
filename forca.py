import random

def jogar():

    titulo()

    palavra_secreta = escolher_palavra()
    letras_acertadas = quantidade_letras(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            chute_certo(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_acertadas)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    if (acertou):
        imprime_mensagem_vencedor()
    elif (enforcou):
        imprime_mensagem_perdedor(palavra_secreta)

    #replay = str(input("Quer jogar de novo? S ou N?").lower())

def titulo():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def escolher_palavra():
    print("(1) Frutas (2) Animais")

    tema = int(input("Qual será o tema? "))

    if (tema == 1):
        lista_frutas = open("frutas.txt", "r", encoding="utf-8")
        frutas = []

        for linha in lista_frutas:
            linha = linha.strip()
            frutas.append(linha)

        lista_frutas.close()

        posicao = random.randrange(0, len(frutas))
        palavra_secreta = frutas[posicao].upper()

    elif (tema == 2):
        lista_animais = open("animais.txt", "r", encoding="utf-8")
        animais = []

        for linha in lista_animais:
            linha = linha.strip()
            animais.append(linha)

        lista_animais.close()

        posicao = random.randrange(0, len(animais))
        palavra_secreta = animais[posicao].upper()
    return palavra_secreta

def quantidade_letras(palavra):
    return ["_" for letra in palavra]  # lista = [] / tuple = (não pode ser alterado)
    # .append() para adicionar um item à lista

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def chute_certo(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
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
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
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

if (__name__ == "__main__"):
    jogar()
