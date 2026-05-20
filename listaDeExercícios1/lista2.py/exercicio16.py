# 16. CAIXA DE SUPERMERCADO

subtotal = 0

for i in range(5):
    preco = float(input(f"Digite o preço do produto {i + 1}: "))
    subtotal += preco

imposto = subtotal * 0.10
valor_final = subtotal + imposto

print("Subtotal:", subtotal)
print("Imposto (100%):", imposto)
print("Valor final:", valor_final)