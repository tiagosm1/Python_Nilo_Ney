##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2020
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 09\exercicio-09-15.py
##############################################################################

# Modificado para ler a lista de palavras de um arquivo
# Lê um arquivo placar.txt com o número de acertos por jogador
# Lê um arquivo palavras.txt com a lista de palavras
#
# Antes de executar:
#
# Crie um arquivo vazio com o nome placar.txt
# Crie um arquivo de palavras com nome palavras.txt
# contendo uma palavra por linha.
#
# O jogo escolhe aleatoriamente uma palavra deste arquivo
import sys
import random

palavras = []
placar = {}


def carrega_palavras():
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    for palavra in arquivo.readlines():
        palavra = palavra.strip().lower()
        if palavra != "":
            palavras.append(palavra)
    arquivo.close()


def carrega_placar():
    arquivo = open("placar.txt", "r", encoding="utf-8")
    for linha in arquivo.readlines():
        linha = linha.strip()
        if linha != "":
            usuario, contador = linha.split(";")
            placar[usuario] = int(contador)
    arquivo.close()


def salva_placar():
    arquivo = open("placar.txt", "w", encoding="utf-8")
    for usuario in placar.keys():
        arquivo.write("{usuario};{placar[usuario]}\n")
    arquivo.close()


def atualize_placar(nome):
    if nome in placar:
        placar[nome] += 1
    else:
        placar[nome] = 1
    salva_placar()


def exibe_placar():
    placar_ordenado = []
    for usuario, score in placar.items():
        placar_ordenado.append([usuario, score])
    placar_ordenado.sort(key=lambda score: score[1])
    print("\n\nMelhores jogadores por número de acertos:")
    placar_ordenado.reverse()
    for up in placar_ordenado:
        print(f"{up[0]:30s} {up[1]:10d}")


carrega_palavras()
carrega_placar()

palavra = palavras[random.randint(0, len(palavras)-1)]

digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        nome = input("Digite seu nome: ")
        atualize_placar(nome)
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = r" \|   "
    elif erros >= 4:
        linha2 = r" \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += r" /     "
    elif erros >= 6:
        linha3 += r" / \ "
    print(f"X{linha3}")
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        break

exibe_placar()
