"""
Retornar um valor na Function
=============================
def nome_funcao():
    return "Valor"
"""
# Chamada da função e impressão do retorno dela.
def cadastrar_produto():
    produto = input("Digite o nome do produto: ")
    produto = produto.casefold()
    produto = produto.strip()
    preco = float(input("Digite o preço do produto: R$"))
    quantidade = int(input("Quantas unidades tem em estoque? "))
    # Retornando todos os valores como uma tupla.
    return produto, preco, quantidade
print(cadastrar_produto())

produto = cadastrar_produto()
print("\nNome do Produto: ", produto[0])
print("Preço: R${:.2f}".format(produto[1]))
print("Estoque: {} Unidades".format(produto[2]))

#Return parametro e argumentos

def soma(num1, num2, num3):
    return num1 + num2+ num3
valor = soma(5, 8, 7)
print("A soma é:", valor)

#Crie um programa que classica bedidas em alcoolicas e nao acoolicas

class Bebida:
    def __init__(self, nome, quantidade, tipo):
        self.nome = nome
        self.quantidade = quantidade
        self.tipo = tipo
        
bebidas = {}

def cadastrar_produto():
    nome = input("Digite a bebida: ")
    quantidade = input("Digite a quantidade: ")
    tipo = input("Digite o tipo da bebida (alcoolica ou nao_acoolica): ")

    if not verificar_tipo_bebida(tipo):
        print("Tipo de bebida inválido")
        return

    bebida = Bebida(nome, quantidade, tipo)
    bebidas[nome] = bebida
    print(f"Bebida {nome} cadastrada com sucesso")
    
def listar_bebidas():
    for i, bebida in enumerate(bebidas.values()):
        print(f"{i}: {bebida.nome} - {bebida.quantidade} - {bebida.tipo}") 
    
def verificar_tipo_bebida(tipo):
    return tipo in ['alcoolica', 'nao_alcoolica']

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar bebida")
        print("2. Listar bebidas")
        print("3. Sair")
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_bebidas()
        elif opcao == '3':
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()

    