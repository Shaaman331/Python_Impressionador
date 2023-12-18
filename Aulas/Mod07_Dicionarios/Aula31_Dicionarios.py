print("Dicionairio")
#Estrutura dicionario = {chave:valor, chave:valor, chave:valor...}
#Nao deve ser usados para pegar itrens em determinada ordem
#Podem  ter valores heterogeneos(varios  tipo de valores dentro de um mesmo dicionario)
#Chaves sao unicas obrigatoriamente
#Mais intuitivoso de trabalhar

mais_vendidos = {"tecnologia":"iphone", "refrigeracao":"ar consul 12000 btu","livros":"Senhor dos aneis"}
vendas_tecnologia = {"iphone" : 15000, "sansung galaxy" : 12000, "tv sansung" : 10000, "ps5": 14300, "tablet": 1720}
qtde_iphone = vendas_tecnologia["iphone"]
livro = mais_vendidos["livros"]
qtde_tv = vendas_tecnologia["tv sansung"]

print(f"O mais vendido é o iPhone e foram feitas {qtde_iphone} unidades.")
print(f"O livro mais comprado foi {livro}.")
print(f"A quantidade de vendas foi {qtde_tv}")

#metodo get
produto = vendas_tecnologia.get("iphone") #retorna None se nao encontrar a chave
if vendas_tecnologia is None:
    print("Produto não cadastrado!")
else:
    print(f"Vendemos Iphone a quantidade de {produto}.")

print(vendas_tecnologia.get("sansung galaxy"))
print("Vendemos {} Sansung Galaxy".format(vendas_tecnologia.get("sansung galaxy")))

if "copo" in vendas_tecnologia:
    print(vendas_tecnologia["copo"])
else:
    print("Copo não esta dentro da lista de produtos de tecnologia.")

if vendas_tecnologia.get("copo") == None:
    print("Copo nao esta na lista de produtos de tecnologia.")
else:
    print(f"O preço do copo é R$ {vendas_tecnologia['copo']}")
    