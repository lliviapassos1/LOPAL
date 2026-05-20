# 15. CONTROLE DE ESTOQUE

produto = input("Digite o nome do produto: ")
quantidade_atual = int(input("Digite a quantidade atual: "))
quantidade_vendida = int(input("Digite a quantidade vendida: "))
estoque_restante = quantidade_atual - quantidade_vendida
print("Produto:", produto)
print("Estoque restante:", estoque_restante)
if estoque_restante < 0:
    print("ALERTA: Estoque negativo!")