class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial
    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("No se puede depositar fondos negativos o nulos, ingrese un valor válido")
        self.__saldo += monto
    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("No se puede retirar fondos negativos o nulos")
        if monto > self.__saldo:
            raise ValueError("Fondos suficientes")
        self.__saldo -= monto

######################
# Probando el código #
######################

cuenta = CuentaBancaria("28042004", 100)

#Prueba depositando dinero
try: 
    cuenta.depositar(500)
    print(f"Saldo después del depósito: {cuenta.obtener_saldo()}")
except ValueError as e:
    print(f"Error: {e}")

try: 
    cuenta.depositar(-500)
    print(f"Saldo después del depósito: {cuenta.obtener_saldo()}")
except ValueError as e:
    print(f"Error: {e}")

#Prueba retirando dinero, teniendo 600 depositados el las pruebas anteriores
try: 
    cuenta.retirar(50)
    print(f"Saldo después del retiro: {cuenta.obtener_saldo()}")
except ValueError as e:
    print(f"Error: {e}")

try: 
    cuenta.retirar(-50)
    print(f"Saldo después del retiro: {cuenta.obtener_saldo()}")
except ValueError as e:
    print(f"Error: {e}")

#Mostrando el numero de la cuenta
print(cuenta.obtener_numero_cuenta())

#Mostrando el saldo de la cuenta
print(cuenta.obtener_saldo())