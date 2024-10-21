class CuentaBancaria:
    #se inicia con el constructor
    def __init__(self, numero_cuenta, saldo_inicial):
        self.__numero_cuenta= numero_cuenta
        self.__saldo_inicial= saldo_inicial

    #se definen los getter para mostrar de manera controlada
    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

    def obtener_saldo(self):
        return self.__saldo_inicial
    
    #se definen los métodos para realizar operaciones bancarias
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("No se puede depositar fondos negativos o nulos")
        self.__saldo_inicial += monto
        print(f"Tu saldo actual es {self.__saldo_inicial}")

    def retirar(self, monto):
        if monto <=0:
            raise ValueError ("No se puede retirar fondos negativos o nulos")
        if monto > self.__saldo_inicial:
            raise ValueError("Fondos insuficientes")
        self.__saldo_inicial -=monto
        print(f"Se ha descontado de tu saldo {monto}, tu saldo disponible es {self.__saldo_inicial}")

cuenta_joel= CuentaBancaria(123456,1000000)

#retirar los # uno a uno para probar los métodos en el objeto cuenta_joel

# print(cuenta_joel.__numero_cuenta)

#print(cuenta_joel.obtener_numero_cuenta())

#print(cuenta_joel.obtener_saldo())

#cuenta_joel.depositar(5000000)
# cuenta_joel.depositar(-800)

#cuenta_joel.retirar(8000000)

#cuenta_joel.retirar(-800)

#cuenta_joel.retirar(750)

