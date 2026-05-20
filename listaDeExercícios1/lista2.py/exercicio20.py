# 20. RELATORIOS DE VENDA
vendas = []

for i in range(5):
    valor = float(input(f"Digite o valor da venda {i + 1}: "))
    vendas.append(valor)

maior_venda = max(vendas)
menor_venda = min(vendas)
total_vendido = sum(vendas)
media = total_vendido / len(vendas)

print("\nRELATÓRIO DE VENDAS")
print("Maior venda:", maior_venda)
print("Menor venda:", menor_venda)
print("Total vendido:", total_vendido)
print("Média das vendas:", media)