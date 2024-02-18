class Circulo():
    PI = 3.14

    def __init__(self, initRaio):
        self.raio = initRaio

    #Metodo para acesso para configurar um novo raio
    def setRaio(self, newRaio):
        self.raio = newRaio

    #Metodo de acesso para retornar o valor atual do raio
    def getRaio(self):
        return self.raio

    #Metodo para calcular area
    # Perceba que iremos fazer o cálculo com os atributos da classe
    # O atributo da classe PI pode ser acessado
    # colocando o nome da classe antes
    def calcArea(self):
        return Circulo.PI * ( self.raio * self.raio )

    #metodo __str__
    def __str__(self):
        return ("Círculo de raio: "+ str(self.raio) + ", área: " + str(self.calcArea()))