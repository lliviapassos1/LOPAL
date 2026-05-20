# 17. LISTA DE TICKETS (CHAMADOS tecnicos)

chamados = [
    "Erro no sistema",
    "Falha no login",
    "Problema na impressora",
    "Internet lenta"
]

print("Chamados atuais:")
for chamado in chamados:
    print("-", chamado)

concluido = input("Digite o chamado concluído: ")

if concluido in chamado:
    chamados.remove(concluido)
    print("Chamado removido com sucesso")
else:
    print("Chamado não encontrado")

print("\nChamados restantes:")
for chamado in chamados:
    print("-", chamado)