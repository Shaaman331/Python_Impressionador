"""
Comparadores
== igual 
!= diferente 
> maior que(>= maior ou igual)
< menor que(<= menor ou ifual)
in texto existente dentro de outro texto
not verifica o contrário da comparação

Obs: Se em alguma condição você não quiser fazer nada,
voce simplismente escrever: pass

"""
faturamento_loja_1 = 2500
faturamento_loja_2 = 2500
email = "luucca@gmail.com"

print("Programa 1")
if faturamento_loja_1 == faturamento_loja_2:
    print("Os faturamentos são iguais")
else:
    print("Os faturamentos são diferentes")
print()

print("Programa2")
if email == "luucca1@gmail.com":
    print("Email correto")
else:
    print("Email errado")
print()

print("Programa 3")
email_usuario = input("Insira seu e-mail: ")
if not "@" in email_usuario: #verificando se o @ não está contido no email
    print("Email invalido")
else:
    pass
