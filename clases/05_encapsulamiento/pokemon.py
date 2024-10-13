dano_placaje = 500
mana_pocion = 100
costo_placaje = 75


class Pokemon:
    def __init__(self, nombre, estamina, inteligencia):
        self.nombre = nombre
        self.__estamina = estamina
        self.__inteligencia = inteligencia
        self.__mana = self.__inteligencia * 10
        self.__salud = self.__estamina * 100

    def recibir_placaje(self):
        self.__salud -= dano_placaje
        print(f"{self.nombre} recibió un placaje")

    def tomar_pocion_mana(self):
        self.__mana += mana_pocion
        print(f"{self.nombre} tomó una poción")

    def esta_vivo(self):
        return self.__salud > 0

    def atacar(self, rival):
        if self.__mana < costo_placaje:
            raise Exception(f"{self.nombre} no puede realizar un placaje")
        self.__mana -= costo_placaje
        rival.recibir_placaje()

    def presentar(self):
        print(f"[{self.nombre}] maná: {self.__mana} salud: {self.__salud}")


mudkip = Pokemon("Mudkip", 20, 5)
charmander = Pokemon("Charmander", 10, 10)

turno = 0

while mudkip.esta_vivo() and charmander.esta_vivo():
    turno += 1
    print(f"Turno {turno}")
    mudkip.presentar()
    charmander.presentar()
    if turno % 2 == 1:
        try:
            mudkip.atacar(charmander)
        except Exception:
            mudkip.tomar_pocion_mana()
    else:
        try:
            charmander.atacar(mudkip)
        except Exception:
            charmander.tomar_pocion_mana()
    print()

if mudkip.esta_vivo():
    print(f"Gana {mudkip.nombre}")
else:
    print(f"Gana {charmander.nombre}")
