class SerVivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def gritar(self):
        print("...")


class Vaca(SerVivo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def gritar(self):
        print("muuu")


class Gato(SerVivo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def gritar(self):
        print("miau")


class Planta(SerVivo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def fotosintesis(self):
        print("Realizando fotosíntesis")


def asustar(ser_vivo):
    print(f"Asustando a {ser_vivo.nombre}")
    ser_vivo.gritar()


betsy = Vaca("Betsy")
kit = Gato("Kit")
spike = Planta("Spike")

seres_vivos = [betsy, kit, spike]

for ser_vivo in seres_vivos:
    asustar(ser_vivo)
