#Temperatura dos servidores
"""
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C.
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
"""
temperatura_maxima = 25
try:
    temperatura_atual = float(input("Digite a temperatura atual: "))
    if temperatura_atual > temperatura_maxima:
        print("Alerta! Temperatura acima do limite permitido.")
    else:
        print("Temperatura ok!")
except:
    print("Insira uma temperatura valida!")