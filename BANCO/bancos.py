class Banco:
    def __init__ (self, nome):
        self.nome = nome
        self.lista_clientes = []
        self.conta = []

    def abre_conta(self, conta):
        self.conta.append(conta)

    def lista_conta(self):
        for conta in self.conta:
            print(conta.resumo())