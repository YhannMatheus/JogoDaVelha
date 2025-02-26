import os
import random

player1 = True
player2 = False

menu = """
Menu de jogo
1 - jogar
2 - atribuições
0 - sair
=>"""
menu2 = """
Olá, bem vindo ao jogo da velha da porãygua, esse é um exemplo de como implementar um jogo da velha em python
não copie o codigo apenas leia-o e implemente o seu do seu jeito.
obrigado por ler até aqui
- Ass: yhann matheus de dio miranda mendes - Co-fundador da Porãygua
=>"""

char1 = "X"
char2 = "O"
jogadas = []

matix = [
    [[1],[2],[3]],
    [[4],[5],[6]],
    [[7],[8],[9]]
    ]

def clear():
    os.system("cls")

def desenharTab(tab:list):
    for i in tab:
        print(f"{i[0]}|{i[1]}|{i[2]}")

def verificar_vitoria(tab: list):
    # Verificar linhas
    for linha in tab:
        if linha[0] == linha[1] == linha[2]:
            return linha[0]

    # Verificar colunas
    for col in range(3):
        if tab[0][col] == tab[1][col] == tab[2][col]:
            return tab[0][col]

    # Verificar diagonais
    if tab[0][0] == tab[1][1] == tab[2][2]:
        return tab[0][0]
    if tab[0][2] == tab[1][1] == tab[2][0]:
        return tab[0][2]
    return None

def menu_principal():
    while True:
        clear()
        print(menu)
        opcao = input()

        if opcao == "0":
            break
        elif opcao == "1":
            jogar()
        elif opcao == "2":
            mostrar_atribuicoes()

def jogar():
    global player1, player2, matix
    clear()
    desenharTab(matix)
    while True:
        if player1:
            jogada = obter_jogada(1)
            atualizar_tabuleiro(jogada, char1)
            player1, player2 = False, True
        else:
            jogada = obter_jogada(2)
            atualizar_tabuleiro(jogada, char2)
            player1, player2 = True, False

        clear()
        desenharTab(matix)
        vencedor = verificar_vitoria(matix)
        if vencedor:
            print(f"Jogador {vencedor} venceu!")
            break
        if all(isinstance(item, str) for row in matix for item in row):
            print("Empate!")
            break

def obter_jogada(jogador):
    return int(input(f"Jogador {jogador}, escolha uma posição (1-9): "))

def atualizar_tabuleiro(jogada, char):
    for i in range(3):
        for j in range(3):
            if matix[i][j][0] == jogada:
                matix[i][j] = char
                return

def mostrar_atribuicoes():
    clear()
    print(menu2)
    input("Pressione Enter para voltar ao menu...")

menu_principal()