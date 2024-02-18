class Quadrado():
    def __init__(self, initLado, initX, initY):
        super().__init__(initX, initY)
        self.lado = initLado

    def setLado(self, newLado):
        self.lado = newLado

    def getLado(self):
        return self.lado

    def calcArea(self):
        return (self.lado * self.lado)

    def __str__(self):
        return ("Quadrado de lados: " + str(self.lado) + ", área: "
                + str(self.calcArea()) + "\n" + "(X, Y) = (" + str(self.getX()) + "," + str(self.getY()) + ")")
