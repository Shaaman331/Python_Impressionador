print('Faturamento do melhor ao pior mes do ano')
meses = ['jan','fev','mar','abr','jun','ju;','ago','set','out','nov','dez']
vendas_1sem = [25000, 29000,2200,17750,15870,19900]
vendas_2sem = [19850, 20210,17540,1555, 49051, 9650]
vendas_1sem.extend(vendas_2sem)
print(vendas_1sem)
maior_valor = max(vendas_2sem)
indice_max = vendas_2sem.index(maior_valor) 
print("O valor mais alto foi", maior_valor,"no mês de", meses[indice_max])  
menor_valor = min(vendas_2sem)  
indice_min = vendas_2sem.index(menor_valor) 
print("O menor valor foi", menor_valor,"no mes de ", meses[indice_min])
fat_total = sum(vendas_1sem)
print("Faturamento Total: R${:,}".format(fat_total))
percentual = maior_valor / fat_total
print("O faturamento total que ocorreu no mês com o maior valor: {:.2%}".format(percentual)) 
print("Cria top 3 de valores ")
top3 = []
print(vendas_1sem)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
maior_valor= max(vendas_1sem)
vendas_1sem.remove(maior_valor)
top3.append(maior_valor)    
maior_valor= max(vendas_1sem)   
maior_valor = max(vendas_1sem)
top3.append(maior_valor)    
print(top3) 
