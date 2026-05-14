#Gerenciador de tarefas
"""
Ana precisa de um programa simples para gerenciar suas tarefas diárias.
Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas.
Use uma lista para armazenar as tarefas.
"""
import os
tarefas = []

def exibir_menu():
    os.system("cls")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    selecionar_opcao()
    
def selecionar_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                adicionar_tarefa()
            case 2:
                visualizar_tarefas()
            case 3:
                remover_tarefa()
            case 4:
                print("Saindo do gerenciador de tarefas. Até mais!")
            case _: 
                print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
                input("Pressione qualquer tecla para retornar ao menu: ")
                exibir_menu()
    except:
        print("Opção inválida")
        input("Pressione qualquer tecla para retornar ao menu: ")
        exibir_menu()



def adicionar_tarefa():
    os.system("cls")
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")
    input("Pressione qualquer tecla para retornar ao menu: ")
    exibir_menu()

def visualizar_tarefas():
    os.system("cls")
    if tarefas:
        print("\nTarefas")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa cadastrada.")
    input("Pressione qualquer tecla para retornar ao menu: ")
    exibir_menu()

def remover_tarefa():
    os.system("cls")
    if not tarefas:
        print("Erro: Nenhuma tarefa para remover.")
        input("Pressione qualquer tecla para retornar ao menu: ")
        exibir_menu()
    try:
        tarefa_para_remover = int(input("Digite o número da tarefa a ser removida: ")) -1
        if 0 <= tarefa_para_remover < len(tarefas):
            removida = tarefas.pop(tarefa_para_remover)
            print(f"Tarefa {removida} removida.")
        else:
            print("Erro: Indice inválido!")
    except ValueError:
        print("Erro: Entrada inválida! Digite um número.")

    input("Pressione qualquer tecla para retornar ao menu: ")    
    exibir_menu()

exibir_menu()