from collections import Counter #Ultilizamos o metodo Counter para contar as ocorrencias

vendas_tecnologia = {" notebook asus": 2450, "notebook del": 2156, "iphone" : 5000, "ps5" : 3500, "tv sansung" : 2350, "tv lg" : 45000 }
aux = Counter(vendas_tecnologia) #A variavel aux armazena o objeto Counter que representa o dicionario vendas tecnoligia
print(f"Venda de Tecnologia: {aux.most_common(3)}") # O metodo most_common() é usado para obter uma lista de itens, classificado por ondem de ocorrencia (3) para obter os itens vendidos
