#simulacion bancaria

class cuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad ):
        self.saldo += cantidad
        print("deposito exitoso. saldo actual:", self.saldo)


    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("retiro exitoso, saldo actual:", self.saldo)
        else:
            print("saldo insuficiente.")

mi_cuenta = cuentaBancaria("carlos", 100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(200)
mi_cuenta.retirar(70)        
