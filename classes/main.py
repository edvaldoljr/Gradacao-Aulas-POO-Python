from classes.Carro import Carro
from classes.ControleRemoto import ControleRemoto
from classes.ClientesNetflix import ClientesNetflix

carro1 = Carro('Ford', 'UNO', "preto")
print("=== Carro === "
      "\n Marca:", carro1.marca,
      "\n Cor:", carro1.cor,
      "\n Modelo", carro1.modelo)

print("\n")

controleRemoto1 = ControleRemoto('preto', '10cm', '2cm', '2cm')
print("=== Controle Remoto === ",
      "\n Cor: ", controleRemoto1.cor,
      "\n Largura: ", controleRemoto1.largura,
      "\n Profundidade: ", controleRemoto1.profundidade,
      "\n Altura: ", controleRemoto1.altura)

print("\n")

clienteNetiflix1 = ClientesNetflix('Edvaldo', 'edjr@gmail.com', 'basic')
print("=== Cliente Netflix === "
      "\n Cliente: ", clienteNetiflix1.nome,
      "\n Email: ", clienteNetiflix1.email,
      "\n Plano: ", clienteNetiflix1.plano)