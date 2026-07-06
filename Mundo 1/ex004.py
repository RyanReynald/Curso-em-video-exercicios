#Dissecando uma Variável

a = input("Digite algo: ")

print("o tipo primitivo desse valor é ", type(a))

print(f"Só tem espaço? {a.isspace()}", )

print("É um numero? {}".format(a.isnumeric()))

print("É alfabético? ", a.isalpha())

print("É alfanumerico? ", a.isalnum())

print("Está em maiusculo? ", a.isupper())

print("Está em minisculo? ", a.islower())

print("Está capitalizada? ", a.istitle())

