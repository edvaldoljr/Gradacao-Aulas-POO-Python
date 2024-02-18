
class ClientesNetflix():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        lista_planos = ["basic", "premium"]
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Inválido")
