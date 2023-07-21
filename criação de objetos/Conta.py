class Conta:
    def __init__(self, titular, numero, saldo):
        self._saldo = 0.0
        self._numero = numero
        self._titular = titular

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo