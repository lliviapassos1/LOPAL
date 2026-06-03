# 15.CONTADOR DE VOGAIS

frase = (input("Digite uma frase:"))
contador = 0
for letra in frase.lower():
    if letra in "aeiou":
        contador += 1
print(f"Quantidade de vogais:{contador}")
