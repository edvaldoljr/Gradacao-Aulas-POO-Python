class FracamentePrivado():
    def __init__(self, initNum, initSaldo):
        self._numero = initNum
        self._saldo = initSaldo

    def _adicionarBonus(self):
        self._saldo += 1000
