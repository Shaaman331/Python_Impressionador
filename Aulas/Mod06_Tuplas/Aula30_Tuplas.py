print("Tuplas")
# Tuplas sao estruturas que acessam variaveis, porem sao imutaveis
# Tuplas sao usadas para guardar varios valores em uma unica variavel
#Vantagens - Mais eficiente (em termos de performace)
#          - Protege a base de dados(por ser imutavel)
#          - Muito usada para dados heterogeneos

vendas = ("Lucca", "01/12/2020", "03/02/1990", 2000,"Estagiario")
print(vendas)

# Acessando os valores da tupla 
nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]
print(nome , data_contratacao, data_nascimento, salario, cargo)


#Usando o enumarete para acessar valores da tupla
vendas = [1000, 2000, 300, 300, 150]
funcionarios = ["Joao","Lucas","Ana","Maria", "Paula"]
for i, venda in enumerate(vendas):
    print(f"O funcionario(a) {funcionarios[i]} vendeu {venda} unidades")
