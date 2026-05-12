#Calculando a idade
"""
Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento.
Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.
"""

def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

try:
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    print(f"Sua idade é {calcular_idade(ano_nascimento, ano_atual)}")
except:
    print("Valor invalido.")