# 12.FATORIAL SIMPLES

numero = int(input("Digite um número inteiro positivo:"))
fatorial = 1
for i in range(1,numero + 1):
    fatorial *= i
print(f"faotrial de {numero} ={fatorial}")
