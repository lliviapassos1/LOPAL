# 5.DESCONTO EM E-BOOKS

valor = float(input("Digite o valor do livro: R$"))
if valor > 80:
  valor_final = valor*0.9
  print(f"Valor com desconto: R${valor_final:.2f}")
else:
    print(f"Valo final: R${valor:.2f}")
