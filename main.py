from conta import Conta
from controller import create, read

# Função inicial do programa. O nome "menu" foi solicitado pelo profesor
def menu():
    
    pessoa = Conta()            # Criando um objeto de Conta()
    
    # Atribuição de valores para o objeto
    pessoa.numero = int(input('Informe o número da conta: '))
    pessoa.titular = str(input('Ingorme o nome do titular: '))
    pessoa.saldo = float(input('Informe o saldo inicial: '))

    # Adiciona atributos do objeto pessoa para o arqiuivo txt 
    create(pessoa)
    
    # Atribuindo informações contidas no arquivo txt via função read()
    lista_contas = read()
    
    # Print com o endereço na memória solicitado pelo professor
    print(lista_contas)
    
    # Print descritivo dos itens contidos no arquivo txt 
    print('\nItens do TXT')
    for c in lista_contas:
        print(f'Titular: {c.titular} > Número: {c.numero} > Saldo: {c.saldo}') 

menu()
