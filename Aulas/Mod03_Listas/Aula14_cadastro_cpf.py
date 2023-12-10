cpf = input('Insira seu CPF(digite apenas numeros)')

#tratar cpf
cpf_sem_pontuacao = cpf.replace('.', '').replace(',','')    
cpf_sem_traco = cpf.replace('-', '')

if len(cpf) == 11:
    print("CPF valido") 
else:
    print('Digite seu CPF corretamente e digite apenas numeros')