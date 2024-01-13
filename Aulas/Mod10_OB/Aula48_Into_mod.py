"""
Modulos 
* Vem com muitas funcionalidades prontas para uso
* Podem ser importados e utilizados em outros módulos do projeto.
* Estrutura Basica 

impor modulo
ou 
import modulo as nome

Modulo Time
time.time() - Retorna o tempo atual em segundos desde 1
"""
import webbrowser as wb
import time

# Abre o navegador na pagina informada
#wb.open('https://www.google.com')
#wb.open("https://www.hashtagtreinamentos.com")

# Modulo Time 
segundos_hoje = time.time()
print(f"Segundos desde a meia noite: {segundos_hoje}")

# Mostra data e hora atuais
data_hoje = time.ctime()
print(f"\nData e Hora Atuais:\n{data_hoje}")

# Duracao do tempo de programa
tempo_incial = time.time()
for i in range(100000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_incial
print(f"\n O programa levou {duracao} segundos para rodas")

# Delay 5 segundo 
print("Comencando")
time.sleep(5)
print("\n Finalizado!")

# Usar gmtime para pegar informcacoes 
data_atual = time.gmtime()
ano = data_atual.tm_year
mes = data_atual.tm_mon
dia = data_atual.tm_mday
hora = data_atual.tm_hour
dia_da_semana = data_atual.tm_wday

print(f"\n\nHoje é dia: {dia} \nMês: {mes} \nAno: {ano}")
