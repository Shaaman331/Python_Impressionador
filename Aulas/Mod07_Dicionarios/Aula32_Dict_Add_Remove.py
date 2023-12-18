"""Adicionar e remover e modificar itens dentro de um dicionario
dicionario = {}
dicionario[chave] = valor
dicionairio.update({cahve: valor. chave:valor}) """

#Adicionar item ao dicionario 

lucro_1tri = {"janeiro": 100000,"fevereiro": 120000,"marco": 90000}
lucro_2tri = {"abril": 88000,"maio":8900,"junho": 120000}

#adcionando 1 intem
lucro_1tri["abril"] = 88000
print(lucro_1tri)
print()

#Adicionando varios itens ou um dicionario a outro
lucro_1tri.update(lucro_2tri)
print(lucro_1tri)
print()

#Adicionando um item ja existente(manual ou pelo update)
lucro_1tri["janeiro"] = 88000
print(lucro_1tri)
print()

#Modificar itens
lucro_1tri["fevereio"]= 85000
lucro_1tri["fevereio"]
print(lucro_1tri)
print()

#Remover itens
lucro_jun = lucro_1tri.pop("junho")
print ("Valor do mês de junho: ", lucro_jun)
print (lucro_1tri)
print ()

funcionarios =["Joao","Maria","Lucas","Ana","Paula","Rute"]
del funcionarios[0]
print(funcionarios)
print()