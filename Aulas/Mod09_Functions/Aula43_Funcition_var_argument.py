"""
Valores padrao de Argumentos
* Nesse caso, voce nao é obrigado a passar o valor para usar a funcao, 
pode usar o valor padrao

def minha_funcao(argumento = valor_padrao):
...
return ...

"""

produtos = ["apple tv", "mac", "iphone x", "apple wach", "tablet"]
produtos.sort()
print(produtos)
produtos.sort(reverse= True)
print(produtos)

def padronizar_codigos(lista_codigos, padrao = "m"):
    for i, item in enumerate (lista_codigos): #pegar o indice da lista
        item = item.replace("  "," ") #Subistituir espaco duplos por espaco unicos
        item = item.strip()
        if padrao == "m":
            item = item.casefold() #Transformar items em "m" minusculos e maiusculos "M"
        elif padrao == "M":
            item = item.upper()
            lista_codigos[i] = item # indice da lista de codigos
    return  lista_codigos

cod_produto = ["ABC12", "ABC34", "abc37"]
print(padronizar_codigos(cod_produto, "M")) #Transformar itens da lista em maiusculo

lista = [10, 20, 30]

for item in lista:
    lista[0] = item + 5 #modificar valor dos items na lista
    item += 5
print(lista)

