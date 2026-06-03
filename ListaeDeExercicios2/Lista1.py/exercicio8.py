# 8.CALCULADORA DE IMC

peso = float(input("Digite o seu peso (Kg):"))
altura = float(input("Digite a sua alura (m):"))
imc = peso / (altura**2)
print(f"IMC = {imc:.2f}")
