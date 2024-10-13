dano_placaje = 500
mana_pocion = 100


class Pokemon:
    def __init__(self, nombre, estamina, inteligencia, agilidad):
        self.nombre = nombre
        self.__estamina = estamina
        self.__inteligencia = inteligencia
        self.agilidad = agilidad
        self.mana = self.__inteligencia * 10
        self.salud = self.__estamina * 100

    def recibir_placaje(self):
        self.salud -= dano_placaje
        print(f"{self.nombre} recibió un placaje")

    def tomar_pocion_mana(self):
        self.mana += mana_pocion
        print(f"{self.nombre} tomó una poción")

    def presentar(self):
        print(f"[{self.nombre}] maná: {self.mana} salud: {self.salud}")


charmander = Pokemon("Charmander", 10, 10, 20)
mudkip = Pokemon("Mudkip", 20, 5, 18)

charmander.presentar()

mudkip.presentar()
mudkip.recibir_placaje()
mudkip.presentar()
mudkip.tomar_pocion_mana()
mudkip.presentar()

charmander.presentar()
