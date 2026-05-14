#Pedra, papel e tesoura
"""
Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador.
Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura.
O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

Pedra ganha de Tesoura (Pedra quebra Tesoura);
Tesoura ganha de Papel (Tesoura corta Papel);
Papel ganha de Pedra (Papel cobre Pedra);
Se ambos escolherem a mesma opção, é um empate.
"""
import random

def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)
    escolha_jogador = input("Escolha: pedra, papel ou tesoura? ").lower()
    if escolha_jogador not in opcoes:
        print("Escolha inválida!")
        return
    print(f"Computador escolheu {escolha_computador}")
    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif(
        escolha_jogador == "pedra" and escolha_computador == "tesoura" or
        escolha_jogador == "tesoura" and escolha_computador == "papel" or
        escolha_jogador == "papel" and escolha_computador == "pedra"
    ):
        print("Você venceu!")
    else:
        print("Você perdeu!")

jogar()