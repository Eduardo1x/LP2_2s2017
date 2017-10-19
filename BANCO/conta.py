class Conta:
    def __init__(self, saldo, clientes, numero):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero       
        self.operacoes = []
        if saldo > 0:
            self.deposito(saldo)


    def resumo(self):
        print('CC número: {}, Saldo {}'
                .format(self.numero, self.saldo))

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            tupla1 = ('saque', valor)
            self.operacoes.append(tupla1)
            #self.operacoes.append(('saque', valor)) poderia ser feito assim!!
    def deposito(self, valor):
        self.saldo += valor
        tupla2 = ('deposito', valor)
        self.operacoes.append(tupla2)
        #self.operacoes.append(('deposito', valor)) poderia ser feito assim!!       

    def extrato(self):
        for extrato1 in self.operacoes:
            print('{} --- {}'.format(extrato1[0], extrato1[1]))
        print('Saldo atual: ', self.saldo)

#c = Conta(100,['Fernando'],12345)
#c.deposito(100)
#print(c.extrato())



#        self.resumo = self.resumo
#        self.saque = self.saque
#        self.deposito = self.deposito
#        self.extrato = self.extrato