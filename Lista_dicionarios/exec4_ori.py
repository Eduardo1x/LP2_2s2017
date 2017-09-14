produtos = {
    'tomate': [100, 2.3],
    'alface': [500, 0.45],
    'laranja': [300, 1.3],
    'cenoura': [130, 2.1],
    'manga': [75, 3.45]
}

tupla_produtos = tuple(produtos.keys())

tupla_produtos = ('tomate', 'alface', 'laranja', 'cenoura', 'manga')

def entrada_produto():
    nome_produto = input('Digite o nome do produto: ')
    if not nome_produto in tupla_produtos:
        if nome_produto == 'fim':
            return -1
        else:
            return None
    else:
        qtd = input('Quantidade: ')
        produto = produtos[nome_produto]
        dic_retorno = {nome_produto: [qtd, produto[1]]}
        return dic_retorno

retorno = 0
lista_compra = []
while retorno != -1:
    retorno = entrada_produto()
    if retorno != -1 and retorno!= None:
        lista_compra.append(retorno)
print(lista_compra)
