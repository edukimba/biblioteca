#LISTAS:

USUARIOS = []
LIVROS =[]
EMPRESTADOS = [] 

#HUB DE OPÇÕES:

def hub():
    while True:
        print("\n---BIBLIOTECA---")
        print("1. ADICIONAR NOVOS LIVRO")
        print("2. REMOVER LIVRO")
        print("3. LISTAR LIVROS DISPONÍVEIS")
        print("4. REGISTRAR USUÁRIOS")
        print("5. REGISTRAR EMPRÉSTIMOS DE LIVROS")
        print("6. CONSULTAR LIVROS DISPONÍVEIS E EMPRESTADOS")
        print("0. SAIR")

        opcao = input("ESCOLHA UMA OPÇÃO:")
        
#OPÇÃO 1

        if opcao == "1":
            print("---------------")
            print(f"VOCÊ ESCOLHEU ADICIONAR NOVO LIVRO!")
            print("---------------")
            livro_novo = input("DIGITE O NOME DO LIVRO NOVO:")
            print("---------------")
            if livro_novo in LIVROS:
                print("LIVRO JÁ CADASTRADO!")
            else:
                print("LIVRO ADICIONADO!")
                LIVROS.append(livro_novo)

#OPÇÃO 2:
        
        elif opcao == "2":
            print("---------------")
            print("VOCÊ ESCOLHEU REMOVER UM LIVRO!")
            print("---------------")
            nome = input("DIGITE O NOME DO LIVRO A SER REMOVIDO")
