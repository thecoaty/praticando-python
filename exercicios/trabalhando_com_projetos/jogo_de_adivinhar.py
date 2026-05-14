#Jogo de adivinhar o número
"""
Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido.
Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada,
impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número.
O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte.
Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .
"""
import random

def adivinha_numero():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    #print(numero_aleatorio)

    while True:
        try:
            tentativa = int(input("Tente adivinhar o número (1-100): "))
            if not 1 <= tentativa <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")

            tentativas += 1
            if tentativa > numero_aleatorio:
                print("Muito alto, tente um número menor!")
            elif tentativa < numero_aleatorio:
                print("Muito baixo, tente um número maior!")
            else:
                print(f"isso ai você acertou o número aleatorio {numero_aleatorio} com {tentativas} temtativas!")
                break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

adivinha_numero()