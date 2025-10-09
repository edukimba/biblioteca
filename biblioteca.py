#LISTAS:

USUARIOS = []
LIVROS = []
EMPRESTADOS = [] 

#HUB DE OPÇÕES:

def hub():
    while True:
        print("\n---BIBLIOTECA---")
        print("1. ADICIONAR NOVO LIVRO")
        print("2. REMOVER LIVRO")
        print("3. LISTAR OS LIVROS DISPONÍVEIS")
        print("4. REGISTRAR NOVO USUÁRIO")
        print("5. REMOVER USUÁRIO")
        print("6. LISTAR USUÁRIOS")
        print("7. REGISTRAR EMPRÉSTIMO DE LIVRO")
        print("8. CONSULTAR LIVROS DISPONÍVEIS E EMPRESTADOS")
        print("0. SAIR")
        print("---------------")

        opcao = input("ESCOLHA UMA OPÇÃO:")
        
#OPÇÃO 1:

        if opcao == "1":
            print("---------------")
            print(f"VOCÊ ESCOLHEU ADICIONAR UM NOVO LIVRO!")
            print("---------------")
            livro_novo = input("DIGITE O NOME DO LIVRO NOVO:").strip().lower()
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
            livro = input("DIGITE O NOME DO LIVRO:" ).strip().lower()
            if livro in LIVROS:
                print("---------------")
                LIVROS.remove(livro)
                print(f"LIVRO'{livro.title()}' REMOVIDO")
            else:
                print("---------------")
                print("LIVRO NÃO ENCONTRADO!")

#OPÇÃO 3:

        elif opcao == "3":
            print("---------------")
            print("VOCÊ ESCOLHEU LISTAR LIVROS DISPONÍVEIS!")
            print("---------------")
            if len(LIVROS) == 0:
                print("NÃO HÁ LIVROS!")
            else:
                for i in range(len(LIVROS)):
                    print(f"{i} - {LIVROS[i].title()}")

#OPÇÃO 4:

        elif opcao == "4":
            print("---------------")
            print(f"VOCÊ ESCOLHEU ADICIONAR UM NOVO USUÁRIO!")
            print("---------------")
            usuario_novo = input("DIGITE O NOME DO USUÁRIO NOVO:").strip().lower()
            print("---------------")
            if usuario_novo in USUARIOS:
                print("USUÁRIO JÁ CADASTRADO!")
            else:
                print("USUÁRIO ADICIONADO!")
                USUARIOS.append(usuario_novo)

#OPÇÃO 5:

        elif opcao == "5":
            print("---------------")
            print("VOCÊ ESCOLHEU REMOVER UM USUÁRIO!")
            print("---------------")
            remover_usuario = input("DIGITE O NOME DO USUÁRIO A SER REMOVIDO:").strip().lower()
            print("---------------")
            if remover_usuario not in USUARIOS:
                print("USUÁRIO NÃO ENCONTRADO!")
            else:
                print("USUÁRIO REMOVIDO!")
                USUARIOS.remove(remover_usuario)

#OPÇÃO 6:

        elif opcao == "6":
            print("---------------")
            print("VOCÊ ESCOLHEU LISTAR TODOS OS USUÁRIOS!")
            print("---------------")
            if len(USUARIOS) == 0:
                print("NÃO HÁ USUÁRIOS!")
            else:
                for i in range(len(USUARIOS)):
                    print(f"{i} - {USUARIOS[i].title()}")

#OPÇÃO 7:

        elif opcao == "7":
            print("---------------")
            print("VOCÊ ESCOLHEU REGISTRAR UM EMPRÉSTIMO!")
            print("---------------")
            livro_emprestado = input("DIGITE O NOME DO LIVRO A SER EMPRESTADO:").strip().lower()
            if livro_emprestado in LIVROS:
                usuario = input("DIGITE O NOME DO USUÁRIO:").strip().lower()
                if usuario in USUARIOS:
                    LIVROS.remove(livro_emprestado)
                    EMPRESTADOS.append({"livro": livro_emprestado, "usuario": usuario})
                    print("---------------")
                    print(f"EMPRÉSTIMO REGISTRADO PARA {usuario.title()}!")
                else:
                    print("---------------")
                    print("USUÁRIO NÃO ENCONTRADO!")
            elif any(e["livro"] == livro_emprestado for e in EMPRESTADOS):
                print("---------------")
                print("LIVRO JÁ ESTÁ EMPRESTADO!")
            else:
                print("---------------")
                print("LIVRO NÃO ENCONTRADO!")

#OPÇÃO 8:

        elif opcao == "6":
            print("---------------")
            print("VOCÊ ESCOLHEU VER LIVROS EMPRESTADOS E DISPONÍVEIS!")
            print("---------------")
            if len(LIVROS) == 0 and len(EMPRESTADOS) == 0:
                print("NÃO HÁ LIVROS!")
            else:
                print("LIVROS DISPONÍVEIS:")
                for i, livro in enumerate(LIVROS):
                    print(f"{i} - {livro.title()}")
                print("---------------")
                print("LIVROS EMPRESTADOS:")
                for i, livro in enumerate(EMPRESTADOS):
                   print(f"{i} - {livro['livro'].title()} (EMPRESTADO PARA {livro['usuario'].title()})")

#OPÇÃO 0:

        elif opcao == "0":
            print("---------------")
            print("SAINDO...")
            break

#OPÇÃO INEXISTENTE SERÁ TRATADA ASSIM:

        else:
            print("---------------")
            print("OPCÃO INVÁLIDA!")

if __name__ == "__main__":
    hub()