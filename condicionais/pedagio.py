#Calculando pedágio
"""
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio.
O valor do pedágio depende da distância percorrida:
Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
"""


try:
    distancia_percorrida = float(input("Digite a distancia percorrida (em km): "))
    if distancia_percorrida < 100.00:
        print("Valor do pedágio: R$10,00")
    elif 100 <= distancia_percorrida <= 200:
        print("Valor do pedágio: R$20,00")
    else:
        print("Valor do pedágio: R$30,00")

except:
    print("Valores invalidos")
    