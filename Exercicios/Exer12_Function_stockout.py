"""
Calcule o stockout de vendas

"""
vendas = {"VE0001":(1500, "Concluido",""),"VE0002":(13300, "Cancelado","Cancelado pelo Cliente"),"VE003":(6007,"Concluido",""),"VE004":(15562,"Concluido",""),
          "VE0005":(18752,"Cancelado","Estoque em Falta"),"VE0006":(16358,"Cancelado","Estoque em Falta"),"VE0007":(17045,"Concluido",""),"VE0008":(12230,"Concluido","")
          ,"VE0010":(6747,"Concluido",""),"VE0011":(15114,"Concluido",""),"VE0012":(12497,"Concluido","")}

def calcula_stockout(dicionario_vendas):   
    numerador = 0
    denominador = 0
    for vendas in dicionario_vendas: #criar unpackt 
        valor, status, motivo = dicionario_vendas[vendas]
        if status == "Concluído": #Se a venda for "Concluido" o valor total da venda é adicionado ao deniminador
            denominador += valor
        elif status == "Cancelado" and motivo == "Estoque em Falta": #Se a venda for "Cancelado" ou "Estoque em falta" o valor total da venda é adiconado ao denominador e numerador
            denominador += valor
            numerador += valor
    return float('%.2f' % (numerador/denominador *1)) #Calcular percentual de vendas

print(calcula_stockout(vendas))

print()

clientes_devedores = [("462.286.561-1",144405,24),("251.569.170-81",16500,1),("297.681.579-21",15000,24),("790.233.154-40",9553,10)]

def clientes_inadiplentes(lista_devedores):
    lista_inadiplentes = []
    for cliente in lista_devedores:
        cpf, valor, dias = cliente
        if valor > 1000 and dias > 20:
            lista_inadiplentes.append((cpf,valor,dias))
    return lista_inadiplentes

print(clientes_inadiplentes(clientes_devedores))

