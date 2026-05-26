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
    usuario_login = input("Usuário: ")
    senha_login = input("Senha: ")

    if senha_login == senha_criada:
        print(f'{usuario_login}, login realizado com sucesso!')
        break
    else: 
        print(f'{usuario_login}, sua senha está incorreta.')
        print("Tente novamente...\n")

# USUARIO CADASTRADO, IDENTIFICADO COM SENHA E COM ACESSO AO INVENTARIO 

print("Bem-vindo ao Inventário de Cibersegurança - UFU")

lista = ['notebook', 'mouse', 'roteador', 'adaptador']

while True:
    print ('Selecione uma opção')
    opcao = input ("[i]nserir [a]pagar [l]istar [s]air: ").lower()

    if opcao == "i":
       valor = input ("Ativo: ")
       lista.append(valor)

       print(f"{valor} adicionado com sucesso!")

    elif opcao == "a":
        valor = input("Qual ativo deseja apagar? ")

        if valor in lista:
            lista.remove(valor)
            print(f"{valor} removido com sucesso!")
        else:
            print("Ativo não encontrado.")


    elif opcao == "l":
       if len(lista) == 0:
          print ("Nada para listar")
    
       else:
           print("\n===== ATIVOS CADASTRADOS =====")

           for i, valor in enumerate(lista):
               print(i, valor)

    elif opcao == "s":

        print("Encerrando inventário...")
        break

    else: 
        print("Por favor, escolha i, a,  l ou s.")

#O SISTEMA PERMITE O USUARIO INSERIR, APAGAR, LISTAR ATIVOS DO INVENTARIO 















