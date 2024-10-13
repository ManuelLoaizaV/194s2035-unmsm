class Brawler:
    nombre_juego = "Brawl stars"

    def __init__(self, nombre, salud, nivel, ataque):
        self.nombre = nombre
        self.salud = salud
        self.nivel = nivel
        self.ataque = ataque
        self.__defensa = salud * nivel

    def recibir_ataque(self, ataque):
        self.salud -= ataque

    def obtener_defensa(self):
        return self.__defensa

    def obtener_puntos(self):
        return 50 * self.nivel

    def obtener_fuerza(self):
        return self.nivel * self.ataque

    def presentar(self):
        print(f"{self.nombre} tiene {self.salud} de vida y está en nivel {self.nivel}")


barley = Brawler("Barley", 3500, 11, 1300)
barley.presentar()

# Solo podemos acceder a atributos privados vía getters
print(barley.obtener_defensa())

# No podemos modificar atributos privados
barley.__defensa = 0
barley.presentar()
