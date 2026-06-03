# 4.ALERTA DE TEMPERATURA

temperatura = float(input("Digite a temperatura do servidor(°C):"))
if temperatura > 75:
    print("ALERTA: superaquecimento!")
else:
    print("Temperatuda normal!")
