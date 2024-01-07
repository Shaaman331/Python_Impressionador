"""
Functions

As functions sao blocos de codigos que servem para 1 unico proposito
Eles permitem a separacao do codigo em partes, tornando o programa mais organizado e facil de entender.

Estrutura Básica
def funcao_nome(parametros):
    # faca alguma coisa
    # faca outra coisa
    return valor_final
    
"""

#Criar uma funcao de cadastro de produtos
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    produto = nome.casefold()
    preco = float(input("Digite o preço do produto: ")) 
    quantidade = int(input("Digite a quantidade do produto: "))
    total = preco * quantidade
    print(f"O produto {produto} custa R$ {total:.2f}")
    

#Function no laco for para cadastrar 3 produtos    
for i in range(3):
    cadastrar_produto()
print("Os produtos foram cadastrados com sucesso")

#Funcao de cadastrar nome cpf e telefone do cliente

#Criando a classe Cliente 
class Cliente:
    def __init__(self, nome, cpf, telefone): #Definindo os atributos nome, cpf e telefone
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

clientes = [] #Os cliente sao armazenados na lista 

#Criando a funcao cadastrar cliente
def cadastrar_cliente(): 
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    cliente = Cliente(nome, cpf, telefone)
    clientes.append(cliente)

    print(f"Cliente {nome} cadastrado com sucesso!")

#Laço For para cadastrar  clientes
def listar_clientes(): # A função listar_clientes itera sobre a lista clientes e exibe as informações de cada cliente.
    print("\nLista de clientes:")
    for cliente in clientes:
        print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Telefone: {cliente.telefone}")

"""
A função main é responsável por executar o laço principal do programa. 
Ela exibe um menu com opções para cadastrar um cliente, listar todos os clientes ou sair do programa. 
Dependendo da opção escolhida pelo usuário, a função chama a função correspondente e exibe o resultado.

"""
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
