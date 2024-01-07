"""
Quantidade indefinidas de Argumentos
Quando voce quer permitir uma quantidade indefinidadas de argumentos, use o * 
*args para posicional arguments -> Argumentos vem em formato de tuplas
def minha_func(*args)
# args é um tuple com todos os argumentos passados na chamada da função.

**kwargs para keyword arguments -> argumentos em formatod de dicionario 
def minha_func(**kwargs): 
# kwargs é um dictionary com todos os argumentos passados na chamada da função

"""

def minha_soma(*numeros):
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma
print(minha_soma(1,2,3),19, 29, 59)

def preco_final (preco, **adicionais):# adicionais é um dictionario com todos os valores adicionais que foram passados
    print(adicionais)
    if "desconto" in adicionais:
        preco *=(1 - adicionais["desconto"])
    if "garantia_extra" in adicionais:
        preco+= adicionais["garantia_extra"]
    if "imposto" in adicionais:
        preco *=(1 + adicionais["imposto"])
    return preco

print(preco_final(1000, desconto = 0.1, garantia_extra = 100, imposto = 0.3))

"""
Ordem dos argumentos 
Estrutura:
* Os positional arguments vem antes e depois dos keywords arguments
* Os argumentos individuais vem antes e depois os "multiplos"

def minha_funcao(arg1, arg2, arg3, *args, k = kwargs1, k2 = kwarg2, k3= kwarg3, **kwargs):

"""
def minha_soma(*numeros, num1):
    soma = 0
    for numero in numeros:
        soma += numero
    soma += num1
    return soma
print(minha_soma(1,2,3,4,5, num1 = 5))
