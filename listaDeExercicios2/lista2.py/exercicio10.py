# 10.REAJUSTE DE BOLSA AUXÍLIO

bolsa = float(input("Digite o valor da bolsa: R$"))
if bolsa < 1000:
    nova_bolsa = bolsa*1.15
else:
    nova_bolsa = bolsa*1.10
print(f"Novo valor da bolsa: R$ {nova_bolsa:.2f}")
