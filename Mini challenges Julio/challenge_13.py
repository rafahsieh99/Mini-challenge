class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto

    def consultar(self):
        return self.saldo

cuenta = CuentaBancaria(200) 
print(f"Saldo inicial: {cuenta.consultar()}")  

cuenta.depositar(200)
print(f"Saldo después de depositar: {cuenta.consultar()}")  

cuenta.consultar()
print(f'Su saldo es de: {cuenta.consultar()}')
