# 14.CARINHO DE COMPRAS

itens = []
while True:
    item = input("Digite um item (ou'sair'para encerrar):")
    if item.lower() == "sair":
        break
    itens.append(item)
print("itens adicionados:")
for item in itens:
    print(item)
    