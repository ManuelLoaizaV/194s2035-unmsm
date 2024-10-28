class Vertebrado:
    def __init__(self, numero_piernas):
        self.__numero_piernas = numero_piernas

    def gritar(self):
        print("RAAA")

    def presentar(self):
        print(f"Tengo {self.__numero_piernas} pierna(s)")


class Perro(Vertebrado):
    def __init__(self):
        super().__init__(4)


class Humano(Vertebrado):
    def __init__(self):
        super().__init__(2)


v = Vertebrado(10)
v.presentar()
v.gritar()

bobby = Perro()
bobby.presentar()

gabriel = Humano()
gabriel.presentar()

paola = Humano()
paola.presentar()

rufus = Perro()
rufus.presentar()
