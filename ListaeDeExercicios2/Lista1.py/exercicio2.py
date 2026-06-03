# 2.TEMPO DE DOWNLOAD

tamanho_mb = float(input("Digite o tamanho do arquivo(MB):"))
velocidade_mbps = float(input("Digite a velocidade da internet(Mbps):"))
tempo_segundos = (tamanho_mb*8)/velocidade_mbps
print(f"Tempo aproximadode download: {tempo_segundos:.2f}segundos")
