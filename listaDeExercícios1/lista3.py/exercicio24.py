# 24. RANKING DE NOTAS
notas = []

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

crescente = sorted(notas)
decrescente = sorted(notas, reverse=True)

print("\nNotas em ordem crescente:")
print(crescente)

print("\nNotas em ordem decrescente:")
print(decrescente)