# 30. SISTEMA COMPLETO 
produtos = []


def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    produtos.append(nome)
    print("Produto cadastrado com sucesso")


def listar_produtos():
    print("\nLISTA DE PRODUTOS")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado")
    else:
        for produto in produtos:
            print("-", produto)


def buscar_produto():
    nome = input("Digite o produto para buscar: ")

    if nome in produtos:
        print("Produto encontrado")
    else:
        print("Produto não encontrado")


def remover_produto():
    nome = input("Digite o produto para remover: ")

    if nome in produtos:
        produtos.remove(nome)
        print("Produto removido")
    else:
        print("Produto não encontrado")


def salvar_arquivo():
    arquivo = open("produtos.txt", "w")

    for produto in produtos:
        arquivo.write(produto + "\n")

    arquivo.close()

    print("Produtos salvos no arquivo")


def ler_arquivo():
    try:
        arquivo = open("produtos.txt", "r")

        conteudo = arquivo.read()

        print("\nCONTEÚDO DO ARQUIVO:")
        print(conteudo)

        arquivo.close()

    except:
        print("Arquivo não encontrado")


while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Remover produto")
    print("5 - Salvar em arquivo")
    print("6 - Ler arquivo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        remover_produto()

    elif opcao == "5":
        salvar_arquivo()

    elif opcao == "6":
        ler_arquivo()

    elif opcao == "0":
        print("Sistema encerrado")
        break

    else:
        print("Opção inválida")