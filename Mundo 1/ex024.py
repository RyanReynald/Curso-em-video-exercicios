#Verificando as primeiras letras de um texto


cidade = str(input("Qual cidade você nasceu? ")).strip().lower().split()

print("santo" in cidade[0])

##print(cidade[:5].lower() == "santos")