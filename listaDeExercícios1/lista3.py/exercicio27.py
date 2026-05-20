# 27. CADASTRO MODULAR
def cadastrar_nome():
    nome = input("Digite o nome: ")
    return nome


def cadastrar_email():
    email = input("Digite o e-mail: ")
    return email


def validar_idade():
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"


nome = cadastrar_nome()
email = cadastrar_email()
situacao = validar_idade()

print("\nDADOS CADASTRADOS")
print("Nome:", nome)
print("E-mail:", email)
print("Situação:", situacao)