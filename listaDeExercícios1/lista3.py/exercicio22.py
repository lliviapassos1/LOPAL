# 22. RESERVA DE ASSENTO
assentos = [
    ["Livre", "Livre", "Livre"],
    ["Livre", "Livre", "Livre"],
    ["Livre", "Livre", "Livre"]
]

print("ASSENTOS DISPONÍVEIS:\n")

for linha in assentos:
    print(linha)

linha = int(input("\nEscolha a linha (0 a 2): "))
coluna = int(input("Escolha a coluna (0 a 2): "))

if assentos[linha][coluna] == "Livre":
    assentos[linha][coluna] = "Ocupado"
    print("\nAssento reservado com sucesso")
else:
    print("\nAssento já está ocupado")

print("\nMATRIZ ATUALIZADA:\n")

for linha in assentos:
    print(linha)