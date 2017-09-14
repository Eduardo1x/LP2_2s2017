from exec4 import entrada_produto

def test_entrada_produtos():
    assert entrada_produto ('cenoura', 10) == {'cenoura':[10,2.1]}
    assert entrada_produto ('tomate', 20) == {'tomate':[20,2.30]}
    assert entrada_produto ('abacate', 3) == None
    assert entrada_produto ('fim', 0) == -1