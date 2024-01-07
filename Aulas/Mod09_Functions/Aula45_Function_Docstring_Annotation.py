"""
Docstring e Annotations 
Sao ferramentas apenas para organizacao 
Quando criamo uma funcao, normalmente nao seremos as unicas pessoas a ultilizar - las
e tambem pode ser que a gente precise usar essa mesma funcao semanas, meses ou anos depois
E se um dia quisermos saber o que aquela variavel representa?
Docstring -> Diz oque a funcao faz, quais valores elatem como argumento e oque significa
Annotations -> Explicam os tipos de dados das variaveis (argumentose funcao)

"""
def minha_soma(num1, num2, num3):
    """
    Faz a soma de 3 numeros inteiros e devolve como resposta um inteiro

    Parameters:
    num1 (int): Primeiro numero a ser somado
    num2 (int): Segundo numero a ser somado
    num3 (int): Terceiro numero a ser somado
    Returns:
    int: A soma dos tres numeros
    """
    return num1 + num2 + num3
print(minha_soma.__doc__) # Mostra todo o docstring da funcao 
minha_soma()
#Anotation: 
""""
def minha_funcao(arg1: isso, arg2: aquilo) -> oque a funcao retorna:
    return .... 

"""
def minha_funcao(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3 
res = minha_funcao(5, 10, 15)
print(f'O resultado foi {res}')

 #print(minha_funcao.__annotations__) # Mostra todos os annotations da 
