# 19.VALIDADOR DE PORTAS DE REDE

while True:
    porta = int(input("Digite uma porta de rede para liberar no firewall: "))
    if porta == 80 or porta == 443:
        print("Porta liberada!")
        break 
    else:
        print("Porta bloqueada, tente outra")