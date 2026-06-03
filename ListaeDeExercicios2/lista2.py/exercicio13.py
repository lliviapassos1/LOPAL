# 13.FILTRO DE DOMÍNIOS

emails = [
    "livia@gmail.com",
    "enzo@gmail.com",
    "campos@gmail.com",
    "passos@gmail.com",
    "passoscampos@gmail"
]
for email in emails:
    if email.endswith("@gmail.com"):
        print(email)
