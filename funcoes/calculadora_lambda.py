#Calculadora com lambda
"""
Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico
de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.
Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático
escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
"""

soma = lambda num1, num2: num1 + num2
subtrai = lambda num1, num2: num1 - num2
multiplica = lambda num1, num2: num1 * num2
divide = lambda num1, num2: num1 / num2 if num2 != 0 else "Erro: Divisão por zero"


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Escolha a operação (| + | - | * | / |): ")

if op == "+":
    print(f"{num1} + {num2} = {soma(num1,num2)}")
elif op == "-":
    print(f"{num1} - {num2} = {subtrai(num1,num2)}")
elif op == "*":
    print(f"{num1} * {num2} = {multiplica(num1,num2)}")
elif op == "/":
    print(f"{num1} / {num2} = {divide(num1,num2)}")
else:
    print("Operação inválida")