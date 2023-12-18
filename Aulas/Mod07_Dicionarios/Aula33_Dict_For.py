""""
For nos Dicionarios
Estrutura:
for chave in dicionario:
    faca algo
"""
print("For em Dicionarios")
vendas_tecnologia = {"iphone": 15000,"sansung galaxy": 12000,"tv sansung": 1000,"ps5": 15000,"tablet": 2500,"notebook hp": 10000,"notebook dell": 17000, "notebook asus": 2450}

for chave in vendas_tecnologia:
    print(f'Produto: {chave} = Valor: {vendas_tecnologia[chave]}')

print()

#Somar valores  

total_notebook = 0 #variavel auxiliar
for chave in vendas_tecnologia:
    if "notebook" in chave:
        total_notebook += vendas_tecnologia[chave]
print(f'O valor total das notebooks é de R$ {total_notebook:.2f}')
print()

