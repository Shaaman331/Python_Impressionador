"""
Blocos e Identação
Estrutura 
Sempre que usamos if ou qualque outra estrutura no Python, devemos usar a identação
para dizer para o Programa onde a estrutura começa e onde ela termina.
Isso vai ajudar quando tivermos mais de 1 condição e ao mesmo tempo quando tivermos 
várias ações para fazer dentro de um if;
"""
meta = 0.05
taxa = 0
redimento = 0.25

if redimento > meta:
    if redimento > 0.20:
        taxa = 0.04
        print("A taxa foi de {}".format(taxa))
    else:
        taxa = 0.02
        print("A taxa foi de {}".format(taxa))
else:
    taxa = 0
    print("A taxa foi de {}.".format(taxa))
"""
Mais de uma condição ao mesmo tempo:
if condiçao_1:
    o que fazer se a condição 1 for verdadeira
if condicao_2:
    o que fazer se a condição 1 e 2 for verdadeira
else:
    o que fazer se a condição 2 for falsa(mais a condição 1 é verdadeira)
else:
    o que fazer se a condição 1 for falsa


Importante: Repetição de código
Sempre que possível, evite repetir código. De forma geral:
"Se você está repetindo código, existe uma forma melhor de se fazer.        
    
"""