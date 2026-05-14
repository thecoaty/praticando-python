#Monitorando vendas no comércio
''''
Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado.
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas.
Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais.
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
'''
try:
    macas = int(input("Digite a quantidade de maçãs vendidas: "))
    bananas = int(input("Digite a quantidade de bananas vendidadas: "))
    if macas == bananas:
        print(f"Houve empate nas vendas, totalizando {macas + bananas} vendas de {macas} maçãs e {bananas} bananas.")
    elif macas > bananas:
        print(f"As maçãs tiveram mais vendas, totalizando {macas}.")
    else:
        print(f"As bananas tiveram mais vendas, totalizando {bananas}.")
except:
    print("Valor invalído")
