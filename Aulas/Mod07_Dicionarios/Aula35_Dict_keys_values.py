"""
Listas para Dicionarios
Metodos importantes:
.keys() -> uma "lista" com todas as chaves do dicionario
.values() -> uma lista com todos os valores do dicionário
"""
vendas_tecnologia = {"notebook asus":2450,"iphone":1500,"sansung galaxy":12000,"tv sansung": 10000,"tablet":1720,"ps5":14300,"notebook dell": 17000,"ipad": 1000,"notebook hp": 1000}

#Acessando chaves e valores do dicionciario
chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()

print()
print(f'Chaves: {chaves}') 
print(f'\nValores: {valores}\n')

#transforamando em listas
chave_list = list(vendas_tecnologia.keys())
valor_list = list(vendas_tecnologia.values())
print('Chaves transformadas em lista:', chave_list)
print('Valores transformados em lista:', valor_list, '\n')

#Adicionando valores a lista
vendas_tecnologia["placa de video"] = 10
print(chaves)
print(valores)
chave_list.append("processador")
print(chave_list)


#Ordenando listas
lista_chaves = list(chaves)
lista_chaves.sort() #Ordenar lista
print(lista_chaves)
