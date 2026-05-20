# 14. CADASTRO MÚLTIPLO DE USUÁRIOS
usuarios - []
for i in range(5):
    nome = input(f"Digite o nome de usuário {i + 1}: ")
    usuarios.append(nome)
print("\nUsuários cadastrados:")
for usuario in usuarios:
    print(usuario)