from modelos.restaurante import Restaurante

rest1 = Restaurante("galber", "japonesa")
rest2 = Restaurante("praça", "Italiana")
rest1.alternar_estado()
rest1.receber_avaliacao("Gui", 10)
rest1.receber_avaliacao("Cley", 8)
rest1.receber_avaliacao("Emy", 5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
