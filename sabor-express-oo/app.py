from modelos.restaurante import Restaurante

rest1 = Restaurante("galber", "japonesa")
rest2 = Restaurante("praça", "Italiana")



def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
