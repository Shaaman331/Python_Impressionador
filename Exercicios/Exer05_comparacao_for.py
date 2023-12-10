print("Criando Registro de pessoas")
qtde_pessoas = int(input("Quantas pesssoas terao no quarto ?"))
quarto = []

for i in range(qtde_pessoas):
    nome = input("Qual o nome ?")
    cpf = input("Qual o cpf ?")
    hospede = [nome, "cpf:{}".format(cpf)]
    quarto.append(hospede)  
    print(quarto)   

print()

print("Analise de vendas")
meta = 1000
vendas = ["Joao",1500],["Julia", 2700],["Marcus",9900],["Maria", 3750],["Ana", 10300],["Alon", 7870]

for item in vendas:
    if item[1] > meta:
        print("Vendedor {} bateu a meta. Fez {} vendas".format(item[0],item[1]))

print()
print("Analise de vendas 2")
produtos = ["iphone","galaxy","ipad","tv","maquina de cafe","kindle","geladeira","adega","notebook dell","notebook hp"]
vendas2019 = [558147, 712350, 405252, 7186454,531580,973139,892292,422760, 154753, 887061]
vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 644913, 539704]
for i, produtos in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        crescimento = vendas2020[i] / vendas2019[i] - 1
        print("{} vendeu R${:,} em 2019, R${:,} em 2020, e teve {:,.1%} de crescimento".format(produtos, vendas2019[i], vendas2020[i], crescimento)) 
