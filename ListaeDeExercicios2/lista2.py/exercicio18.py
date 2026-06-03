# 18.DETECTOR DE PALÍDROMO

palavra = input("Digite uma palavra:").lower()

if palavra == palavra[::-1]:
    print("É um políndromo!")
else:
    print("Não é um políndromo!")