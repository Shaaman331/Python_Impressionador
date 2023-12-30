""""
Metodo Set
* É uM método que se utiliza para agregar o eliminar elementos de uma colecao.
* Nao pode ter valores duplicados
* Nao tem ordem fixa

Estrutura
meu_set = {valor, valor, valor, valor, ....}

"""

# Metodos do SET
set_produtos = {"arroz", "feijao", "macarrao", "atum"}
print(set_produtos)
# Adicionando um elemento no set    
set_produtos.add("leite")  # adicionado com sucessso
print(set_produtos)
print()

cpf_clientes = ["520.316.130-57","569.127.380-95", "522.220.330-12","738.967.670-11","252.377.420-84"]
set_cpf_clientes = set(cpf_clientes)
print("Temos {} clientes na loja".format (len(set_cpf_clientes))) # Retorna <class 'set'>

