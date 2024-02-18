#Criando um objeto da classe Cachorro
from heranca02.Cachorro import Cachorro
from heranca02.Pessoa import Pessoa

# Criando um objeto da classe Cachorro

meu_cachorro = Cachorro("Bolinha", 3, "Labrador")

# Acessando atributos e métodos da classe base

print(meu_cachorro.nome)  # Imprime: Bolinha

print(meu_cachorro.idade)  # Imprime: 3

meu_cachorro.falar()  # Imprime: O Bolinha está falando.

# Acessando atributos e métodos da classe derivada

print(meu_cachorro.raca)  # Imprime: Labrador

meu_cachorro.latir()  # Imprime: O Bolinha está latindo.

pessoa = Pessoa("Luiz", 20)
pessoa.falar()
