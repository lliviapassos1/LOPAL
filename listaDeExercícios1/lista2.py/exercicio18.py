# '8. MENU INTERATIVO
usuarios = []

while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        usuarios.append(nome)
        print("Usuário cadastrado")

    elif opcao == "2":
        print("\nUsuários cadastrados:")
        for usuario in usuarios:
            print(usuario)

    elif opcao == "3":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida")