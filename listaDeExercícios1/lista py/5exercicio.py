# 5. SISTEMA DE LOGIN
usuario_correto = "admin"
senha_correta = "1234"
usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == 1234:
    print("Login realizado com sucesso")
else:
    print("Credenciais invalidas")