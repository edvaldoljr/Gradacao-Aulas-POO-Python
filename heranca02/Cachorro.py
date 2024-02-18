from heranca02.Pessoa import Pessoa


class Cachorro(Pessoa):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        #f antes da string indica que é uma f-string.
        print(f"O {self.nome} está latindo")