#Começo do codigo com funçoes input, print e f string. Aprendizado de coleta de dados e utilização de variavéis
nome = input ("Insira seu nome: ")

print(f'Olá, {nome}!')

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


#ENUM - TIPOS de ATIVOS
from  enum import Enum

class TipoAtivo(Enum): 

    SOFTWARE = "Software"
    HARDWARE = "Hardware"
    ESTACAO = "Estação de trabalho"
    BANCO = "Banco de dados"

# Severidades permitidas
severidades_validas = ["Baixa","Média","Alta","Crítica"]


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
    print("1 - Inserir ativo")
    print("2 - Listar ativos")
    print("3 - Lista ativos ordenados")
    print("4 - Buscar ativo")
    print("5 - Atualizar ativo")
    print("6 - Remover ativo")
    print("7 - Sair")

#Cadastrar
def cadastrar_ativos(ativos):
    try:
        id_ativos = int(input("ID do Ativo "))

        if id_ativos in ativos:
            print("ID já cadastrado")
            return
        
        print("\n Tipos disponíveis: ")
        
        for tipo in TipoAtivo: 
            print(tipo.value)


        tipo_ativo = input ('Tipo de ativo:').title()
        if tipo_ativo not in [tipo.value for tipo in TipoAtivo]:
            print("Tipo inválido")
            return
        objeto = input ("Nome do ativo: ")
        responsavel = input("Responsável pelo ativo: ")
        vulnerabilidade = input ("Vulnerabilidade do ativo: ")
        severidade = input ("Severidade (Baixa/Média/Alta/Crítica): ")
        if severidade not in severidades_validas:
            print("Severidade inválida")
            return
        
        ativos[id_ativos] = {
            "Ativo": objeto,
            "Tipo de ativo": tipo_ativo,
            "Responsável": responsavel,
            "Vulnerabilidade": vulnerabilidade,
            "Severidade": severidade
        }

        # Salvamento em arquivo TXT

        with open(
            "ativos.txt",
            "a",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(
                f'{id_ativos};'
                f'{objeto};'
                f'{tipo_ativo};'
                f'{responsavel};'
                f'{vulnerabilidade};'
                f'{severidade}\n'
            )

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
        print(f'Tipo de ativo: {dados["Tipo de ativo"]}')
        print(f'Responsável: {dados["Responsável"]}')
        print(f'Vulnerabilidade: {dados["Vulnerabilidade"]}')
        print(f'Severidade: {dados["Severidade"]}')


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

#LOCALIZAR ATIVO POR ID CADASTRRADO
def localizar_ativos(ativos):
    try:

        if not ativos:
            print("Nenhum ativo cadastrado.") 
            return
        
        id_ativos = int(input("Digite o ID do ativo: "))

        if id_ativos in ativos:
            dados = ativos [id_ativos]

            print("\n ------ ATIVO LOCALIZADO-------")
            print (f'\nAtivo: {dados["Ativo"]}')
            print(f'Tipo de ativo: {dados["Tipo de ativo"]}')
            print (f'Responsável: {dados["Responsável"]}')
            print (f'Vulnerabilidade: {dados["Vulnerabilidade"]}')
            print(f'Severidade: {dados["Severidade"]}')


        else: 
            print("Ativo não encontrado.")

    except ValueError:
        print("ID inválido")

#Atualizar inventario 

def atualizar_ativos(ativos):
    try: 
        id_ativos = int(input("ID do ativo a atualizar: "))

        if id_ativos not in ativos:
            print("Ativo não encontrado")
            return
        print("Deixe em branco para manter o valor atual")

        nome = input (f'Nome ({ativos[id_ativos] ["Ativo"]}):')
        if tipo_ativo not in [tipo.value for tipo in TipoAtivo]:
            print("Tipo inválido")
            return
        tipo = input (f'Tipo({ativos[id_ativos] ["Tipo de ativo"]}):')
        responsavel = input (f'Responsável ({ativos[id_ativos] ["Responsável"]}):')
        vulnerabilidade = input (f'Vulnerabilidade ({ativos[id_ativos] ["Vulnerabilidade"]}):')
        severidade = input (f'Severidade ({ativos[id_ativos] ["Severidade"]}):')
        if severidade not in severidades_validas:
            print("Severidade inválida")
            return
        
        if nome: 
            ativos[id_ativos]["Ativo"] = nome
        if tipo: 
            ativos[id_ativos]["Tipo de ativo"] = tipo
        if responsavel:
            ativos[id_ativos]["Responsável"] = responsavel
        if vulnerabilidade:
            ativos[id_ativos]["Vulnerabilidade"] = vulnerabilidade
        if severidade:
            ativos[id_ativos]["Severidade"] = severidade
            

        print ("Ativo atualizado com sucesso!")

    except ValueError:
        print("Dados inseridos inválidos.")

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
        case '4': #BUSCAR
            localizar_ativos(ativos)
        case '5':
            atualizar_ativos(ativos) 
        case '6':
            apagar_ativo(ativos) 
        case '7': 
            print("Saindo...")
            break
        case _:
            print("Digite uma opção válida!")


             






        
        







































































