#Gerador de funções personalizadas
"""
Miguel está desenvolvendo um sistema de cupons de desconto
e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
Diante deste problema, crie uma closure que gere uma função capaz de calcular
o preço final com um desconto fixo definido pelo usuário.
"""

def desconto(valor_desconto):
    def calcular_desconto(valor_compra):
        return valor_compra - (valor_compra * (valor_desconto/100))
    return calcular_desconto

valor_desconto = float(input("Digite a porcentagem de desconto: "))  
calcular_preco_final = desconto(valor_desconto) 
valor = float(input("Digite o valor da compra: "))  
print(f"Preço final com desconto: {calcular_preco_final(valor)}") 