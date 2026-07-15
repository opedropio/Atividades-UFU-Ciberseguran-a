import json

#--->Sistema Login de acesso

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.senha = None

    def criar_senha(self):
        self.senha = input("Crie uma senha de acesso: ")
        print(f"{self.nome}, senha criada com sucesso")

    def fazer_login(self):
        while True:
            print(f"Usuário: {self.nome}")
            senha_login = input("Senha: ")
            if senha_login == self.senha:
                print(f"{self.nome}, login realizado com sucesso!")
                return
            print(f"{self.nome}, sua senha está incorreta.")
            print("Tente novamente...\n")


nome = input("Insira seu nome: ")
print(f'Olá, {nome}!')
usuario = Usuario(nome)

while True:
    entrada = input(f'{usuario.nome}, você deseja "Entrar" ou "Sair"?').strip().lower()

    if entrada == "entrar":
        print("Você deve criar um acesso ao sistema")
        usuario.criar_senha()
        break
    elif entrada == "sair":
        print("Você saiu do sistema")
        exit()
    else:
        print("Desculpe, digite apenas entrar ou sair")
        print("Retornando ao menu inicial...\n")

print(" REALIZE O LOGIN")
usuario.fazer_login()
print("Bem-vindo ao Inventário de Cibersegurança - UFU")

#-----> Sistema inventário

class Ativo: 
    #Ativos serão os objts a serem cadastrados
    def __init__(self, nome, id_ativo, tipo_ativo, responsavel, vulnerabilidade, severidade):
        #__init__ é o método construtor, usado para iniciar o primeiro atributo.
        self.nome = nome
        self.id_ativo = id_ativo
        self.tipo_ativo = tipo_ativo
        self.responsavel = responsavel 
        self.vulnerabilidade = vulnerabilidade
        self.severidade = severidade

class Inventario:
    def __init__(self, arquivo="inventario.json"):
        self.arquivo = arquivo
        self.ativos = []
        self.carregar()

    def salvar(self):
        dados = [ativo.__dict__ for ativo in self.ativos]
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def carregar(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
            self.ativos = [Ativo(**d) for d in dados]
        except FileNotFoundError:
            self.ativos = []
        except json.JSONDecodeError:
            print(f"{usuario.nome}, o arquivo {self.arquivo} está corrompido. Iniciando inventário vazio.")
            self.ativos = []


    def cadastrar_ativo(self): 
        print("Cadastro de novo ativo: ")
        while True:
            nome = input("Nome: ").strip()

            if nome:
                break

            print(f"{usuario.nome}, o ativo deve ter um nome!")
        while True:
            try:
                id_ativo = int(input("ID: "))
                break
            except ValueError:
                print(f"{usuario.nome}, digite apenas números.")    
        
        #Para evitar IDs iguais 
        for ativo in self.ativos:
            if ativo.id_ativo == id_ativo:
                print("Esse ID já existe.")
                return
        tipo = input ("Tipo: ")
        responsavel = input("Responsável: ")
        vulnerabilidade = input ("Vulnerabilidade: ")
        while True:
            severidade = input("Severidade (Baixa/Média/Alta/Crítica): ").strip().lower()
            if severidade.lower() in ["baixa", "média", "media", "alta", "crítica", "critica"]:
                break
            print("Severidade inválida")

        ativo = Ativo(nome, id_ativo, tipo, responsavel, vulnerabilidade, severidade)

        self.ativos.append(ativo) #metodo append para add ativo na lista
        self.salvar()
        print(f'Usuário, ativo {nome} cadastrado com sucesso!\n')

    def listar_ativos(self):

        if not self.ativos:
            print("Nenhum ativo cadastrado.")
            return
        
        print("Lista de ativos cadastrados: ")

        for ativo in self.ativos:

            print("---------------------")
            print(f'Nome: {ativo.nome}')
            print(f'ID: {ativo.id_ativo}')
            print(f'Tipo: {ativo.tipo_ativo}')
            print(f"Responsável: {ativo.responsavel}")
            print(f'Vulnerabilidade: {ativo.vulnerabilidade}')
            print(f'Severidade: {ativo.severidade}')

    def buscar_ativo(self): 
        if not self.ativos:
            print(f"{usuario.nome}, nenhum ativo cadastrado.")
            return
        
        id_busca = int(input(f"{usuario.nome}, digite o ID do ativo: "))

        for ativo in self.ativos:
            if ativo.id_ativo == id_busca: 

                print(f"{usuario.nome}, o ativo {id_busca} foi encontrado\n")
                print("---------------------")
                print(f'Nome: {ativo.nome}')
                print(f'ID: {ativo.id_ativo}')
                print(f'Tipo: {ativo.tipo_ativo}')
                print(f"Responsável: {ativo.responsavel}")
                print(f'Vulnerabilidade: {ativo.vulnerabilidade}')
                print(f'Severidade: {ativo.severidade}')
                return
        print(f"{usuario.nome}, ativo {id_busca} não encontrado")


    def atualizar_ativo(self):
        if not self.ativos:
            print(f"{usuario.nome}, nenhum ativo cadastrado.")
            return
        
        id_busca = int(input(f"{usuario.nome}, digite o ID do ativo que deseja atulizar: "))

        for ativo in self.ativos: 
            if ativo.id_ativo == id_busca:

                print ("Deixe em branco para manter o valor atual.\n")
                nome = input(f"Nome ({ativo.nome}): ")
                tipo = input(f"Tipo ({ativo.tipo_ativo}): ")
                responsavel = input(f"Responsável ({ativo.responsavel}): ")
                vulnerabilidade = input(f"Vulnerabilidade ({ativo.vulnerabilidade}): ")
                severidade = input(f"Severidade ({ativo.severidade}): ")

                if nome:
                    ativo.nome = nome

                if tipo:
                    ativo.tipo_ativo = tipo

                if responsavel:
                    ativo.responsavel = responsavel

                if vulnerabilidade:
                    ativo.vulnerabilidade = vulnerabilidade

                if severidade:
                    ativo.severidade = severidade

                print(f"Ativo {ativo.id_ativo} atualizado com sucesso!")
                self.salvar()
                return
        print("Ativo não encontrado.")

    def excluir_ativo(self):

        if not self.ativos:
            print("Nenhum ativo cadastrado.")
            return

        id_busca = int(input("Digite o ID do ativo: "))

        for ativo in self.ativos:
            if ativo.id_ativo == id_busca:
                self.ativos.remove(ativo)
                self.salvar()
                print("Ativo removido com sucesso!")
                return

        print("Ativo não encontrado.")


inventario = Inventario()

while True:
    print("\n===== INVENTÁRIO =====")
    print("1 - Cadastrar ativo")
    print("2 - Listar ativos")
    print("3 - Buscar ativo")
    print("4 - Atualizar ativo")
    print("5 - Excluir ativo")
    print("0 - Sair")

    opcao = input(f"{usuario.nome}, escolha uma opção: ")

    if opcao == "1":
        inventario.cadastrar_ativo()

    elif opcao == "2":
        inventario.listar_ativos()

    elif opcao == "3":
        inventario.buscar_ativo()

    elif opcao == "4":
        inventario.atualizar_ativo()

    elif opcao == "5":
        inventario.excluir_ativo()

    elif opcao == "0":
        print(f"{usuario.nome}, você saiu do sistema de inventário Ciber/UFU.")
        break

    else:
        print("Opção inválida.")
