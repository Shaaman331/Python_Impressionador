#Enumerate permite que você percorra uma lista e ao mesmo tempo tenha em uma variável o índice daquele item

funcionarios = ['Maria','José','Antônio','João','Francisco','Ana','Luiz','Paulo','Caio','Manorel']
for funcionario in funcionarios:
    print(f'O nome do funcionário é {funcionario}.')    

print('-------------------------')  
#Exemplo de como funciona a enumeração com enumerate    
for indice, funcionario in enumerate(funcionarios):            
        print(f'{indice} é o nome do funcionário {funcionario}')

print('------------------------')

print("Controle de estoque")

estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 999, 900, 880, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi','guarana','skol','brahma', 'dell vale', 'dolly', 'red bull', 'cachaca', 'vinho']
nivel_minimo = 50
for indice, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
         print(f"Produto {produtos[indice]} está abaixo do nível mínimo.")  
         