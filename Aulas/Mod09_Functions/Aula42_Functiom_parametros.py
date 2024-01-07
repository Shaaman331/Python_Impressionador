"""
Exemplos de parametros 
uper() -> Nao tem parmetros
sort() -> Apenas paremtros keyword
extend(lista) -> 1 parametro obrigatorio

"""
categoria_bebidas = ["beb123445", "BEB234543", "beb234343", "BEB123434" ]

def categoria_bebidas(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return f'{bebida} é da Categoria Bebidas.'
    else:
        return 'Codigo Invalido para essa Bebida!'



cod_produto = "beb12345"
print(cod_produto.upper())

#lista para short e extend

vendas_ano = [100, 200, 50, 90, 240, 300, 55, 10, 789, 60]
vendas_ano.sort(reverse = True) #Aplicando sort reverso
vendas_nov_dez= [500, 765, 567]
vendas_nov_dez.extend(vendas_nov_dez) #Aplicando o extend
print(vendas_ano)

categoria_bebidas = ["beb123445", "BEB234543", "beb234343", "BEB123434" ]

def categoria_bebidas(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return f'{bebida} é da Categoria Bebidas.'
    else:
        return 'Codigo Invalido para essa Bebida!'

print(categoria_bebidas("beb234343", "BEB")) # Returns: "beb234343 é da Categoria Bebidas."
print(categoria_bebidas("beb123445", "beb")) # Returns: "beb123445 é da Categoria Bebidas."
print(categoria_bebidas("beb234343", "BEB2")) # Returns: "Codigo Invalido para essa Bebida!"