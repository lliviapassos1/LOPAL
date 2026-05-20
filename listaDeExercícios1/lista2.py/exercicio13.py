# 13. VALIDADOR DE SENHA ( COM while)
senha = input("Digite sua senha: ")
while len(senha) < 8:
    print("Senha inválida. Deve ter no mínimo 8 caracteres.")
    senha = input("Digite outra senha: ")
    print("Senha válida!")