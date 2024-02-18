from metodos.Circulo import Circulo

circulo1 = Circulo(5)
print(Circulo.PI)
print(circulo1.getRaio())
circulo1.setRaio(10)
print(circulo1.getRaio())
print("ÁREA: ", circulo1.calcArea())
print(dir(Circulo)) #Listando metodos juntamente os especiais
print(circulo1)