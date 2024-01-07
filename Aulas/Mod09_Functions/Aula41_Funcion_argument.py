"""
Formar parametros e argumentos
Estrutura
- Funcao que recebe os parametros e argumentos
- Cria um dicionario com as informacoes dos parametros e argumentos
- Retorna o dicionário com as informações

2 formas de passar o argumento:
1 - Em ordem(positional argument)
2 - Por nome (keyword argument)

"""

def verificar_bebida_acoolica(bebida):
    return bebida.startswith("BEB")

produtos = ["CAR463854", "TFA 64715", "BEB45510", "TFA44968", "CAR75488", "BEB344556"]

# Chamada da função com argumento posicional
for produto in produtos:
    if verificar_bebida_acoolica(produto):
        print(f"Enviar {produto} para setor de bebida acoolicas")
    else:
        print(f"{produto} não é uma bebida acoolica")
    

print("\n")

def bebida_categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if "BEB" in bebida:
        return True
    else:
        return False

produtos = ["CAR463854", "TFA 64715", "BEB45510", "TFA44968", "CAR75488", "BEB344556", "beb32234455", "bsa3348", "BEB9741","BSA96915"]

for produto in produtos:
    if bebida_categoria(produto, "BEB"):
        print(f"Produto {produto} é alcoolico.")
    elif bebida_categoria(produto, "BSA"):
        print(f"Produto {produto} não é alcoolico.")

