"""
Elif 
E se temos mais de uma caso sim e não ?
E se tivermos 3 casos ?
Usamos o elif da seguinte forma:

if condicao:
    o que fazer se a condiçao 1 for verdadeira
elif condicao_2:
    O que fazer se a condicao 1 for falsa e a condicao 2 for verdadeira
else:
    O que fazer se a condicao 1 e a condicao 2 forem falsas


"""
meta = 20000
vendas = 50000

if vendas < meta:
    print("Não ganhou bonus")
elif vendas > (meta * 2):
    bonus = 0.07 * vendas
    print("Ganhou {} de bonus.".format(bonus))
else:
    bonus = 0.3 * vendas
    print("Ganhou {} de bonus.".format(bonus))
