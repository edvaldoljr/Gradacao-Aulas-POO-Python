class FortementePrivado():
    def __init__(self,initNum,initSaldo):
        self._FortemetePrivado__saldo = initSaldo
        self.__numero = initNum
        self.__saldo = initSaldo

    def getSalfo(self):
        return str(self.__saldo)

    def __adicionarBonus(self):
        self.__saldo += 1000