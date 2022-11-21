from conta import Conta

# Função que criada para "escrever" os atributos do objeto pessoa no arquivo txt
def create(conta):
    
    contas = open('arquivo.txt', 'a')      # Abre 
    contas.write(f'{conta}\n')                          # Escreve
    contas.close()                                      # Fecha
    

# Função que criada para "ler" as linhas do arquivo txt
def read():
    
    lista_contas = list()       # lista_contas é uma lista
    # variável contas recebe o arquivo txt
    contas = open('arquivo.txt', 'r')      # "r" = read
    
    # Loop para percorrer cada "linha/conta" contida na variável contas
    for conta in contas:
        conta = conta.strip()           # Remoção dos espaços do inicio e fim da "linha"
        conta_objeto = conta.split(';') # Fatiamento da string 
        # conta_objeto é uma lista
        
        
        # Objeto de conta
        conta = Conta()
        conta.titular = conta_objeto[0]     # titular
        conta.numero = conta_objeto[1]      # numero
        conta.saldo = conta_objeto[2]       # saldo
        # Atribuindo cada indice da lista conta_objeto para atributos do objeto
        
        # Adicionando o objeto ao fim da lista lista_contas
        lista_contas.append(conta)
    contas.close()          # Fecha
    return lista_contas     # Retorna uma lista com objetos
