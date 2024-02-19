#from encapsulamento.FracamentePrivado import FracamentePrivado
# Se tentarmos executar diretamente os elementos fracamente privados, teremos um erro:
#conta1 = FracamentePrivado(1,1200) #cria a conta
# conta1.numero #o atributo não “existe”
# AttributeError: ‘Conta’ object has no attribute ‘numero’
# conta1.adicionarBonus()
# AttributeError: ‘Conta’ object has no attribute ‘adicionarBonus’
from encapsulamento.FortementePrivado import FortementePrivado

# Como falamos, os atributos/métodos ficam ocultos, logo, se colocar o “_” na
# chamada, conseguimos acesso a ambos:
#conta1 = FracamentePrivado(1, 1200)
#print(conta1._numero)

#Vamos tentar agora acessar os atributos/métodos como fizemos anteriormente,
#porém, agora vamos utilizar dois underscores “__”:
#conta1 = FortemetePrivado(1,1200) #cria o objeto
#conta1.__saldo
# AttributeError: ‘Conta’ object has no attribute ‘__saldo’
#conta1.__adicionarBonus()
# AttributeError: ‘Conta’ object has no attribute ‘__adicionarBonus’


#Nestes exemplos, vimos que não podemos acessar nem mesmo colocando os
#dois “__”, mas existe um recurso que nos permite acessar tais elementos “privados”.
#Vamos utilizar _NomeClasse__nomeAtributo ou _NomeClasse__nomeMétodo.

conta1 = FortementePrivado(1,200)
print(conta1._FortementePrivado__saldo)
conta1._FortementePrivado__adicionarBonus() #chama o método
conta1.FortementePrivado #retorna 2200

