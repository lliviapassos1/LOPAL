# 25. REGISTRO DE LOGS
arquivo = open("logs.txt", "w")

arquivo.write("Sistema iniciado\n")
arquivo.write("Usuário autenticado\n")
arquivo.write("Processo finalizado\n")

arquivo.close()

print("Logs gravados com sucesso")