from conta import Conta
from bancos import Banco
from cliente import Cliente

cliente1 = Cliente('ana', '55555')
cliente2 = Cliente('Bernado', '22222')

conta1 = Conta(100, [cliente1,cliente2], 123456)
conta2 = Conta(200, [cliente2], 1234562)

banco1 = Banco('Banco ITAU')
banco1.abre_conta(conta1)
banco1.abre_conta(conta2)

banco1.lista_conta()
conta1.deposito(50)
banco1.lista_conta()
conta2.saque(130)
banco1.lista_conta()
conta2.resumo()
conta1.resumo()
conta2.extrato()