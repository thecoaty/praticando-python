#Calculando a gorjeta em um restaurante
"""
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta.
O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada
e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta.
O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.
"""

def calcular_conta(valor_conta, valor_gorjeta):
    total_gorjeta = (valor_conta * (valor_gorjeta / 100))
    print(f"Valor da gorjeta: {total_gorjeta}")
    total_conta = valor_conta + total_gorjeta
    return total_conta

valor_conta = float(input("Digite o valor da conta: "))
valor_gorjeta = float(input("Digite a porcentagem de gorjeta: "))
total_conta = calcular_conta(valor_conta, valor_gorjeta)
print(f"Total a pagar: {total_conta}")