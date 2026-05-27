#Começo do codigo com funçoes input, print e f string. Aprendizado de coleta de dados e utilização de variavéis
nome = input ("Insira seu nome: ")

print(f'Olá, {nome:}!')

# Aprendizado de condidicionais if, elif e else
#Tratamento de erro através dos metodos strip e lower, para letrar MAI e MIN
#Estrutura de repetição WHILE e BREAK

while True:  

    entrada = input(f'{nome:} , você deseja "Entrar" ou "Sair"?').strip().lower()


    if entrada == "entrar":
        print("Você deve criar um acesso ao sistema")
#Se o usuario optar por entrar no sistema e ter acesso ao inventario ele deve criar uma senha de acesso
        senha_criada = input ("Crie uma senha de acesso: ")
        print(f'{nome}, senha criada com sucesso')
        break
    elif entrada == "sair":
        print("Você saiu do sistema")
        exit() # Encerra o programa de vez, impedindo que vá para a tela de login
    else:
        print("Desculpe, digite apenas entrar ou sair")
        print("Retornando ao menu inicial...\n") 
 #FAZER O USUARIO VOLTAR AO COMEÇO


 #ESPAÇO DE LOGIN NO SISTEMA DE INVENTARIO

print(" REALIZE O LOGIN")

while True:
    print(f"Usuário:{nome} ")
    usuario_login = nome
    senha_login = input("Senha: ")

    if senha_login == senha_criada:
        print(f'{nome}, login realizado com sucesso!')
        break
    else: 
        print(f'{usuario_login}, sua senha está incorreta.')
        print("Tente novamente...\n")
print("Bem-vindo ao Inventário de Cibersegurança - UFU")
# USUARIO CADASTRADO, IDENTIFICADO COM SENHA E COM ACESSO AO INVENTARIO 


#MENU DE ACESSO AO INVENTARIO 

ativos = {}

def menu():
    print("\n ----- LISTA DE ATIVOS INVENTARIO CIBER -----")
    print("1 - Inserir")
    print("2 - Listar")
    print("3 - Lista por ordem")
    print("4 - Atualizar")
    print("5 - Remover")
    print("6 - Sair")

#Cadastrar
def cadastrar_ativos(ativos):
    try:
        id_ativos = int(input("ID do Ativo "))

        if id_ativos in ativos:
            print("ID já cadastrado")
            return
        objeto = input ("Nome do ativo: ")
        responsavel = input("Responsavel pelo ativo: ")
        vulnerabilidade = input ("Vulnerabilidade do ativo: ")
        
        ativos[id_ativos] = {
            "Ativo": objeto,
            "Responsável": responsavel,
            "Vulnerabilidade": vulnerabilidade
        }

        print(f'{objeto} cadastrado com sucesso!')

    except ValueError:
        print("Ativo inválido.")

#cadastrar_ativos(ativos)

#Listar    
def listar_ativos(ativos):
    if not ativos: 
        print("Nenhum ativo cadastrado.")
        return
    
    for id_ativos, dados in ativos.items():
        print("\n-----------------")
        print(f'ID: {id_ativos}')
        print(f'Nome: {dados["Ativo"]}')
        print(f'Responsável: {dados["Responsável"]}')
        print(f'Vulnerabilidade: {dados["Vulnerabilidade"]}')


#Listar ordenadamente
def listar_ativos_ordenados(ativos):
    if not ativos: 
        print("Nenhum ativo cadastrado.")
        return
    ordenados = sorted(ativos.items(), key= lambda item: item [1] ["Ativo"])

    print ('\n ---- Ativos ordenados por nome ------')
    for id_ativos, dados in ordenados: 
        print(f'{dados["Ativo"]} ({id_ativos})')

#listar_ativos(ativos)
#listar_ativos_ordenados(ativos)

#Atulizar inventario 

def atualizar_ativos(ativos):
    try: 
        id_ativos = int(input("ID do ativo a atulizar"))

        if id_ativos not in ativos:
            print("Ativo não encontrado")
            return
        print("Deixe em branco para manter o valor atual")

        nome = input (f'Nome ({ativos[id_ativos] ["Ativo"]}):')
        responsavel = input (f'Responsável ({ativos[id_ativos] ["Responsável"]}):')
        vulnerabilidade = input (f'Vulnerabilidade ({ativos[id_ativos] ["Vulnerabilidade"]}):')

        if nome: 
            ativos[id_ativos]["Ativo"] = nome
        if responsavel:
            ativos[id_ativos]["Responsável"] = responsavel
        if vulnerabilidade:
            ativos[id_ativos]["Vulnerabilidade"] = vulnerabilidade

        print ("Ativo atulizado com sucesso!")

    except ValueError:
        print("Dados inderidos inválidos.")

#atualizar_ativos(ativos)
#listar_ativos(ativos)


#DELETE

def apagar_ativo(ativos):
    try:
        id_ativos = int (input('ID do ativo para remover: '))

        if ativos.pop(id_ativos, None):
            print("Ativo removido com sucesso.")
        else:
            print("Ativo não encontrado.")

    except ValueError:
        print("Id inválido")

#apagar_ativo(ativos)
#listar_ativos(ativos)

while True:
    menu()
    opcao = input ("Escolha uma opção: ")

    match opcao: 
        case '1': 
            cadastrar_ativos(ativos) 
        case '2': 
            listar_ativos(ativos) 
        case '3': 
            listar_ativos_ordenados(ativos) 
        case '4':
            atualizar_ativos(ativos) 
        case '5':
            apagar_ativo(ativos) 
        case '6': 
            print("Saindo...")
            break
        case _:
            print("Digite uma opção válida!")


             






        
        







































































