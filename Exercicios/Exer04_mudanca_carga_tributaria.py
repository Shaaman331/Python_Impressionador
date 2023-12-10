print("Mudanca de carga tributaria")
#cada item da lista dos produtos corresponde a quantidade de vendas no mes e preco, nessa ordem. 

produtos = ['computador', 'livro','tablet','celular','ar condicionado','alexa','maquina de cafe', 'kindle']

produtos_ecommerce = [
    [10000, 2500],
    [5000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    index_livro = produtos.index('livro') 
    total_antigo = produtos_ecommerce[index_livro] [0] * produtos_ecommerce[index_livro] [1]
    produtos_ecommerce[index_livro][1] = produtos_ecommerce [index_livro][1] * 1.1  
    novo_total = produtos_ecommerce[index_livro] [0] * produtos_ecommerce[index_livro][1]
    print('Será pago a mais de imposto:tR$ {:,}'.format(novo_total - total_antigo))
