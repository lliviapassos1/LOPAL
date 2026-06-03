# 16.ANÁLISE DE LATÊNCIA

pings = [45, 32, 110, 28, 55]

maior = max(pings)
menor = min(pings)
media = sum(pings) / len(pings)

print(f"Maior tempo:{maior}ms")
print(f"Menor tempo:{menor}ms")
print(f"Média:{media:.2f}ms")
