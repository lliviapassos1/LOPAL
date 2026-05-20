# 29. DASHBORAD SIMPLES
vendas = [
    [120, 300, 250],
    [400, 150, 600]
]

total_geral = 0
maior_venda = 0

for linha in vendas:
    total_linha = sum(linha)

    print("Total da linha:", total_linha)

    total_geral += total_linha

    if max(linha) > maior_venda:
        maior_venda = max(linha)

print("\nTotal geral:", total_geral)
print("Maior venda:", maior_venda)