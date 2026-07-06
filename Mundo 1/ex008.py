#Conversor de Medidas

valor = float(input("Uma distância em metros: "))

dm =  valor*10
cm = valor*100
mm = valor*1000
dam = valor/10
hm = valor/100
km = valor/1000

print(f""" 
a medida de {valor} metros é igual a {dm} decímetros
a medida de {valor} metros é igual a {cm} centrímetros
a medida de {valor} metros é igual a {mm} milímetros
a medida de {valor} metros é igual a {dam} decâmetros
a medida de {valor} metros é igual a {hm} hectômetros  
a medida de {valor} metros é igual a {km} quilômetros   
""")