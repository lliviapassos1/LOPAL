# 17.URA ELETRÔNICA

livia = 0
enzo = 0

while True:
    voto = int(input("1 = Lívia | 2 = Enzo |0 = Encerrar:"))

    if voto == 0:
       break
    elif voto == 1:
       livia += 1
    elif voto == 2:
       enzo += 1
print(f"Quantidade de voto livia {livia}")
print(f"Quantidade de voto enzo {enzo}")