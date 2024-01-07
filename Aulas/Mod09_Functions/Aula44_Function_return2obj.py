"""
Return 2 objetos
Retornar como uma tupla com 2 itens
"""
def operacoes_basicas(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 
    return (soma, subtracao, multiplicacao, divisao)

print(operacoes_basicas(10, 2))

