# 28. MINI SISTEMA DE BOLETIM
alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input("Digite a nota: "))

    alunos.append([nome, nota])

print("\nALUNOS APROVADOS:")

for aluno in alunos:
    nome = aluno[0]
    nota = aluno[1]

    if nota >= 7:
        print(nome, "-", nota)