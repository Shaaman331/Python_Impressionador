#Um loop for é usado para iterar uma sequência (que é uma lista, uma tupla, um dicionário, um conjunto ou uma string).

for i in  range(5):
    print("Hello World")


produtos = ['coca', 'pepsi', 'guarana','sprite','fanta']
producao = [1500, 1200,1300,5000, 250]
tamanho = len(produtos)
for i in range(tamanho):
    print(f"Foram produzidas {producao[i]} unidades de {produtos[i]} ")
    
