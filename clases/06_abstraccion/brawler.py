import secrets

for i in range(10):
    r = secrets.randbelow(100)
    print(f"Pseudoaleatorio {i + 1}: {r}")


class Brawler:
    def __init__(self, nombre, x, y, rapidez, energia):
        self.__nombre = nombre
        self.__x = x
        self.__y = y
        self.__rapidez = rapidez
        self.__energia = energia

    def super_mover_arriba(self):
        self.__error_si_no_energia()
        self.__consumir_energia()
        self.mover_arriba()
        self.mover_arriba()

    def super_mover_abajo(self):
        self.__error_si_no_energia()
        self.__consumir_energia()
        self.mover_abajo()
        self.mover_abajo()

    def super_mover_izquierda(self):
        self.__error_si_no_energia()
        self.__consumir_energia()
        self.mover_izquierda()
        self.mover_izquierda()

    def super_mover_derecha(self):
        self.__error_si_no_energia()
        self.__consumir_energia()
        self.mover_derecha()
        self.mover_derecha()

    def __error_si_no_energia(self):
        if self.__energia == 0:
            raise Exception("Energía insuficiente")

    def __consumir_energia(self):
        self.__energia -= 1

    def mover_arriba(self):
        self.__y += self.__rapidez

    def mover_abajo(self):
        self.__y -= self.__rapidez

    def mover_izquierda(self):
        self.__x -= self.__rapidez

    def mover_derecha(self):
        self.__x += self.__rapidez

    def presentar(self):
        print(f"{self.__nombre}. Coordenadas: ({self.__x}, {self.__y}). Energía: {self.__energia}")  # noqa


kenji = Brawler("Kenji", 3, 4, 2, 10)
kenji.presentar()
kenji.mover_arriba()
kenji.presentar()
kenji.super_mover_derecha()
kenji.presentar()
kenji.mover_arriba()
kenji.presentar()
kenji.super_mover_derecha()
kenji.presentar()
kenji.super_mover_derecha()
kenji.presentar()
kenji.super_mover_abajo()
kenji.presentar()

mortis = Brawler("Mortis", 0, 0, 4, 2)
mortis.presentar()
mortis.mover_abajo()
mortis.presentar()
mortis.super_mover_abajo()
mortis.presentar()
mortis.super_mover_abajo()
mortis.presentar()
mortis.super_mover_derecha()
mortis.presentar()
