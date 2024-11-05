class Humano:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__salud = 10

    def obtener_nombre(self):
        return self.__nombre

    def obtener_salud(self):
        return self.__salud

    def sufrir(self, dano):
        self.__salud -= dano


class Tirador(Humano):
    def __init__(self, nombre, municion):
        super().__init__(nombre)
        self.__municion = municion

    def obtener_municion(self):
        return self.__municion

    def consumir_municion(self, n):
        if n > self.__municion:
            raise Exception("Munición insuficiente")
        self.__municion -= n


class Delincuente(Tirador):
    def __init__(self, nombre, municion):
        super().__init__(nombre, municion)

    def disparar(self, objetivo):
        self.consumir_municion(3)
        objetivo.sufrir(3)
        print(f"{objetivo.obtener_nombre()} ahora tiene {objetivo.obtener_salud()} de vida")


class Policia(Tirador):
    def __init__(self, nombre, municion):
        super().__init__(nombre, municion)

    def alertar(self):
        self.consumir_municion(1)
        print("Manos arriba")


daira = Tirador("Daira", 5)
manuel = Humano("Manuel")
eddy = Tirador("Eddy", 8)
alessandro = Humano("Alessandro")
evelin = Tirador("Evelin", 10)

print(eddy.obtener_nombre())
print(alessandro.obtener_nombre())
print(evelin.obtener_municion())

gabriel = Delincuente("Gabriel", 50)
gabriel.disparar(manuel)
gabriel.disparar(manuel)
gabriel.disparar(evelin)

hilary = Policia("Hilary", 100)
hilary.alertar()
hilary.alertar()
hilary.alertar()
hilary.alertar()
