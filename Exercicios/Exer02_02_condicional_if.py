"""
Calculo de bonus
Crie um program que calcule e dê print no bônus
que os funcionários devem receber:
"""
vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= 1000:
    print("O funcionário 1 ganhou {} de bônus".format(vendas_funcionario1 * 0.1))
else:
    print("O funcionário 1 ganhou {} de bônus".format(0))

if vendas_funcionario2 >= 1000:
    print("O funcionário 2 ganhou {} de bônus".format(vendas_funcionario2 * 0.1))
else:
     print("O funcionário 2 ganhou {} de bônus".format(0))

if vendas_funcionario3 >= 1000:
    print("O funcionário 3 ganhou {} de bônus".format(vendas_funcionario3 * 0.1))
else:
     print("O funcionário 3 ganhou {} de bônus".format(0))
print()

print("Codigo melhorado")
if vendas_funcionario1 >= 1000:
    print("O funcionário 1 ganhou {} de bônus".format(vendas_funcionario1 * 0.1))
else:
    bonus = 0
    print("O funcionário 2 ganhou {} de bônus".format(bonus))

if vendas_funcionario2 >= 1000:
    bônus = vendas_funcionario2 * 0.1
else:
    bonus = 0
    print("O funcionário 2 ganhou {} de bônus".format(bonus))

if vendas_funcionario3 >= 1000:
        print("O funcionário 3 ganhou {} de bônus".format(vendas_funcionario3 * 0.1))
else:
    bonus = 0
    print("O funcionário 3 ganhou {} de bônus".format(bonus))

"""
Calculo de bônus com nova regra
Crie um program que calcule e dê print no bônus
Obs: Há 2 formas de fazer, com if dentro de if ou enbtão com if e elif.
"""
if vendas_funcionario1 >= 1000:
     if vendas_funcionario1 >= 2000:
        bonus = 0.15 * vendas_funcionario1
     else:
         bonus = 0.1 * vendas_funcionario1
else:
    bonus = 0
print("O funcionário 1 ganhou {} de bônus".format(bonus))
print()

print("2 maneira if -> elif")

if vendas_funcionario2 >= 2000:
    bonus = 0.15 * vendas_funcionario2
elif vendas_funcionario2 >= 1000:
    bonus = 0.1 * vendas_funcionario2
else:
    bonus = 0
    print("O funcionário 2 ganhou {} de bônus".format(bonus))

if vendas_funcionario3 >= 1000:
     if vendas_funcionario3 >= 2000:
        bonus = 0.15 * vendas_funcionario3
     else:
         bonus = 0.1 * vendas_funcionario3
else:
    bonus = 0
print("O funcionário 3 ganhou {} de bônus".format(bonus))

