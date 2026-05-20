# 26. LEITURA DE LOGS
arquivo = open("logs.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()