# 19. VERIFICADOR DE NUMEROS
pares = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        pares += 1

print("Quantidade de números pares:", pares)