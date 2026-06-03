# 7.CLASSE DE IP

octeto = int(input("Digite o primeiro octeto do IP:"))

if 1 <= octeto <= 126:
  print("Classe A")

elif 128 <= octeto <= 191:
    print("Classe B")
elif 192 <= octeto <= 223:
    print("Classe C")
else:
    print("Classe não encontrada!")
