# 23. SISTEMA DE AUTENTICAÇÃO
tentativas = 0

while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "admin" and senha == "1234":
        print("Login realizado com sucesso")
        break
    else:
        tentativas += 1
        print("Credenciais inválidas")

if tentativas == 3:
    print("Conta bloqueada")