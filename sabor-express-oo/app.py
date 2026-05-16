from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

rest1 = Restaurante("galber", "japonesa")
rest2 = Restaurante("praça", "Italiana")
bebida_suco = Bebida("Suco de Melancia", 5.0, "500Ml")
prato_pizza = Prato("Pizza", 45.00, "Pizza Grande")
bebida_suco.aplicar_desconto()
prato_pizza.aplicar_desconto()
rest1.adicionar_no_cardapio(prato_pizza)
rest1.adicionar_no_cardapio(bebida_suco)

def main():
    rest1.exibir_cardapio

if __name__ == "__main__":
    main()
