#Controlando o orçamento mensal
"""
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos.
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas.
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
"""

gasto_maximo = 3000.00

try:
    total_mes = float(input("Digite o total de despesas do mês (R$): "))
    if total_mes < gasto_maximo:
        print(f"Otimo! você gastou menos que o limite do orçamento, sobrando: {gasto_maximo - total_mes}")
    else:
        print("Atenção você ultrapassou o limite do orçamento.")
except:
    print("Valor invalido!")