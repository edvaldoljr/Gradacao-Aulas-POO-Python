from heranca01.FormaGeometrica import FormaGeometrica


class Circulo(FormaGeometrica):
    PI = 3.14
    def __init__(self, initRaio, initX, initY):
        #Precisamos chamar o __init__ da classe pai
        super().__init__(initX, initY)
        self.raio = initRaio

    def setRaio(self, newRaio):
        self.raio = newRaio

    def getRaio(self):
        return self.raio

    def calcArea(self):
        return Circulo.PI * (self.raio * self.raio)

    def __str__(self):
        return ("Círculo de raio: " + str(self.raio) + ", área: " + str(self.calcArea())
                +"\n"+ "(X, Y) = ("+str(self.getX())+", "+str(self.getY())+")")