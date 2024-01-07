"""
Execoes e Erros em Funcoes 
Como "testar" erros e tratar excecoes:
try:
# codigo que pode gerar um erro
except: # 
    captura todos os tipos de exception
"""

def descobrir_servidor(email):
    try: #Verifica se a algum erro
        posicao_a = email.index("@")
        servidor = email[posicao_a:]
        if "gmail" in servidor:
            return "gmail"
        elif "hotmail" in servidor or "outlook" in servidor:
            return "hotmail"
        elif "yahoo" in servidor:
            return "yahoo"
        elif "uol" in servidor or "bol" in servidor:
            return "uol"
        else:
            return "Nao determinado"
    except: # ocorre quando nao ha @ ou . no email
        raise Exception("Erro digitado nao tem o @, digite novamente.")
    
email = input("Qual seu email ?")
print(descobrir_servidor(email))

print("Codigo melhorado")
def verificar_email(email):
    #Tratamento de strings vazias e dominios incompletos
    if not email or "@" not in email:
        raise Exception("Digite um e-mail valido, incluindo o @")
    
    #Separando o domino do e-mail:
    posicao_a = email.indexI("@")
    servidor = email[posicao_a + 1:]
    
    #Verificando se o dominio temirna com um dominio de nivel superior
    if "." not in servidor[5:]:
        raise Exception("O domínio do e-mail parece estar incompleto. Por favor, inclua o domínio de nível superior, como .com, .org ou .net.")

    # Provedores de e-mail com suporte
    provedores = {"gmail": "gmail", "hotmail": "hotmail", "outlook": "hotmail", "yahoo": "yahoo", "uol": "uol", "bol": "uol"}

    # Procurando o provedor de e-mail no domínio do e-mail
    for provider, suffix in provedores.items():
        if provider in servidor:
            return suffix

    return "Não determinado"